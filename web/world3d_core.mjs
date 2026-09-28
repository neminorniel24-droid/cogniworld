// Pure logic for the 3D viewer (no THREE / DOM dependencies), so it can be
// unit-tested with `node --test tests/js/`. world3d.html does the rendering.

export const HEIGHT_SCALE = 12;

// indexed by biome id: plains, river, mountain, desert, cave
export const BIOME_COLORS = [
  [0.42, 0.66, 0.31],
  [0.24, 0.52, 0.78],
  [0.62, 0.62, 0.64],
  [0.90, 0.78, 0.42],
  [0.42, 0.31, 0.23],
];
const RIVER = 1;

/**
 * Turn elevation/biome grids (n x n, indexed [y][x]) into flat typed arrays
 * for a THREE.BufferGeometry. Grid x -> world x, grid y -> world z.
 */
export function buildTerrain(elevation, biome, heightScale = HEIGHT_SCALE) {
  const n = elevation.length;
  const positions = new Float32Array(n * n * 3);
  const colors = new Float32Array(n * n * 3);
  const heights = new Float32Array(n * n);

  for (let y = 0; y < n; y++) {
    for (let x = 0; x < n; x++) {
      const i = y * n + x;
      let h = elevation[y][x] * heightScale;
      const b = biome[y][x];
      if (b === RIVER) h -= 0.6; // rivers carve a shallow channel
      heights[i] = h;
      positions[i * 3] = x;
      positions[i * 3 + 1] = h;
      positions[i * 3 + 2] = y;
      const c = BIOME_COLORS[b] ?? BIOME_COLORS[0];
      const shade = 0.8 + 0.4 * elevation[y][x]; // higher ground reads a bit lighter
      colors[i * 3] = Math.min(1, c[0] * shade);
      colors[i * 3 + 1] = Math.min(1, c[1] * shade);
      colors[i * 3 + 2] = Math.min(1, c[2] * shade);
    }
  }

  const indices = new Uint32Array((n - 1) * (n - 1) * 6);
  let k = 0;
  for (let y = 0; y < n - 1; y++) {
    for (let x = 0; x < n - 1; x++) {
      const a = y * n + x, b = a + 1, c = a + n, d = c + 1;
      indices[k++] = a; indices[k++] = c; indices[k++] = b; // wound so normals face +y (up)
      indices[k++] = b; indices[k++] = c; indices[k++] = d;
    }
  }

  const heightAt = (x, y) => {
    const xi = Math.min(n - 1, Math.max(0, Math.round(x)));
    const yi = Math.min(n - 1, Math.max(0, Math.round(y)));
    return heights[yi * n + xi];
  };
  return { n, positions, colors, indices, heightAt };
}

// ---- agent appearance -------------------------------------------------

export const MODES = ["infection", "energy", "goal", "emotion"];
export const EMOTION_NAMES = ["fear", "hunger", "curiosity", "contentment"];

const INFECTION = {
  susceptible: [0.92, 0.96, 1.0],
  infected: [1.0, 0.23, 0.23],
  recovered: [0.70, 0.53, 1.0],
};
const GOAL = {
  "seeking food": [1.0, 0.75, 0.2],
  "fleeing danger": [1.0, 0.3, 0.3],
  "exploring": [0.3, 0.85, 1.0],
  "resting": [0.6, 0.6, 0.9],
};
const EMOTION = [
  [1.0, 0.3, 0.3],   // fear
  [1.0, 0.6, 0.1],   // hunger
  [0.3, 0.85, 1.0],  // curiosity
  [0.6, 1.0, 0.6],   // contentment
];
const FALLBACK = [0.8, 0.8, 0.8];

const lerp = (a, b, t) => a + (b - a) * t;

export function dominantEmotion(values) {
  let best = 0;
  for (let i = 1; i < values.length; i++) if (values[i] > values[best]) best = i;
  return best;
}

export function agentColor(mode, agent, maxEnergy = 200) {
  switch (mode) {
    case "infection":
      return INFECTION[agent.infection] ?? FALLBACK;
    case "goal":
      return GOAL[agent.goal] ?? FALLBACK;
    case "emotion":
      return EMOTION[dominantEmotion(agent.emotion ?? [])] ?? FALLBACK;
    case "energy": {
      const t = Math.min(1, Math.max(0, agent.energy / maxEnergy));
      // red (starving) -> yellow -> white (full)
      if (t < 0.5) {
        const u = t / 0.5;
        return [1.0, lerp(0.15, 0.9, u), lerp(0.15, 0.2, u)];
      }
      const u = (t - 0.5) / 0.5;
      return [1.0, lerp(0.9, 1.0, u), lerp(0.2, 1.0, u)];
    }
    default:
      return FALLBACK;
  }
}

// infected agents are drawn larger in every mode so outbreaks stand out
export function agentScale(agent) {
  return agent.infection === "infected" ? 1.6 : 1.0;
}

// ---- smoothing --------------------------------------------------------

/**
 * Move a rendered position `cur` ({x, z}) toward `target` ({x, z}) each frame.
 * Agents respawn at random tiles, so a big jump snaps instead of sliding
 * across the whole map.
 */
export function stepToward(cur, target, alpha = 0.25, snapDist = 4) {
  const dx = target.x - cur.x, dz = target.z - cur.z;
  if (Math.abs(dx) + Math.abs(dz) > snapDist) {
    cur.x = target.x; cur.z = target.z;
  } else {
    cur.x += dx * alpha; cur.z += dz * alpha;
  }
  return cur;
}
