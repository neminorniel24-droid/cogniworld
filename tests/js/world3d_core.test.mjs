import test from "node:test";
import assert from "node:assert/strict";
import {
  buildTerrain, agentColor, agentScale, stepToward, dominantEmotion,
  BIOME_COLORS, HEIGHT_SCALE,
} from "../../web/world3d_core.mjs";

const grid = (n, f) => Array.from({ length: n }, (_, y) => Array.from({ length: n }, (_, x) => f(x, y)));

test("terrain array sizes match an n x n grid", () => {
  const n = 5;
  const t = buildTerrain(grid(n, () => 0.5), grid(n, () => 0));
  assert.equal(t.positions.length, n * n * 3);
  assert.equal(t.colors.length, n * n * 3);
  assert.equal(t.indices.length, (n - 1) * (n - 1) * 6);
});

test("every triangle index is a valid vertex", () => {
  const n = 6;
  const t = buildTerrain(grid(n, (x, y) => (x + y) / 10), grid(n, () => 0));
  for (const i of t.indices) assert.ok(i >= 0 && i < n * n);
});

test("triangles face upward (normal has positive y)", () => {
  const n = 4;
  const t = buildTerrain(grid(n, () => 0.3), grid(n, () => 0));
  const p = (i) => [t.positions[i * 3], t.positions[i * 3 + 1], t.positions[i * 3 + 2]];
  for (let k = 0; k < t.indices.length; k += 3) {
    const [a, b, c] = [p(t.indices[k]), p(t.indices[k + 1]), p(t.indices[k + 2])];
    const u = [b[0] - a[0], b[1] - a[1], b[2] - a[2]];
    const v = [c[0] - a[0], c[1] - a[1], c[2] - a[2]];
    const ny = u[2] * v[0] - u[0] * v[2];
    assert.ok(ny > 0, `triangle ${k / 3} faces down`);
  }
});

test("grid x maps to world x and grid y maps to world z", () => {
  const n = 4;
  const t = buildTerrain(grid(n, () => 0), grid(n, () => 0));
  const i = 2 * n + 3; // y=2, x=3
  assert.equal(t.positions[i * 3], 3);
  assert.equal(t.positions[i * 3 + 2], 2);
});

test("height scales with elevation and rivers are carved lower", () => {
  const n = 3;
  const elev = grid(n, () => 0.5);
  const biome = grid(n, (x) => (x === 1 ? 1 : 0)); // middle column is river
  const t = buildTerrain(elev, biome);
  assert.equal(t.heightAt(0, 0), 0.5 * HEIGHT_SCALE);
  assert.ok(t.heightAt(1, 0) < t.heightAt(0, 0));
});

test("heightAt clamps out-of-range coordinates instead of throwing", () => {
  const t = buildTerrain(grid(3, () => 1), grid(3, () => 0));
  assert.equal(t.heightAt(-5, 99), t.heightAt(0, 2));
});

test("unknown biome ids fall back to plains color", () => {
  const t = buildTerrain(grid(2, () => 0), grid(2, () => 99));
  assert.ok(Math.abs(t.colors[0] - BIOME_COLORS[0][0] * 0.8) < 1e-6);
});

test("infection mode colors the three states distinctly", () => {
  const s = agentColor("infection", { infection: "susceptible" });
  const i = agentColor("infection", { infection: "infected" });
  const r = agentColor("infection", { infection: "recovered" });
  assert.notDeepEqual(s, i);
  assert.notDeepEqual(i, r);
  assert.ok(i[0] > i[1] && i[0] > i[2]); // infected is red-dominant
});

test("energy mode goes from red (starving) to bright (full)", () => {
  const low = agentColor("energy", { energy: 5 });
  const mid = agentColor("energy", { energy: 100 });
  const high = agentColor("energy", { energy: 200 });
  assert.ok(low[1] < 0.3);          // little green -> red
  assert.ok(mid[1] > low[1]);
  assert.ok(high[2] > mid[2]);      // approaches white
});

test("energy outside [0, max] is clamped, never produces invalid colors", () => {
  for (const e of [-50, 0, 200, 9999]) {
    for (const ch of agentColor("energy", { energy: e })) assert.ok(ch >= 0 && ch <= 1);
  }
});

test("goal and emotion modes use their own palettes", () => {
  assert.deepEqual(agentColor("goal", { goal: "resting" }), [0.6, 0.6, 0.9]);
  assert.deepEqual(agentColor("emotion", { emotion: [0.1, 0.9, 0.2, 0.3] }), [1.0, 0.6, 0.1]); // hunger
});

test("unknown mode or missing data falls back to grey", () => {
  assert.deepEqual(agentColor("nope", {}), [0.8, 0.8, 0.8]);
  assert.deepEqual(agentColor("goal", { goal: "???" }), [0.8, 0.8, 0.8]);
});

test("dominantEmotion picks the largest value", () => {
  assert.equal(dominantEmotion([0.1, 0.2, 0.9, 0.3]), 2);
  assert.equal(dominantEmotion([0.5, 0.5]), 0);
});

test("infected agents are drawn larger", () => {
  assert.ok(agentScale({ infection: "infected" }) > agentScale({ infection: "susceptible" }));
});

test("stepToward glides for small moves and snaps for big jumps", () => {
  const cur = { x: 0, z: 0 };
  stepToward(cur, { x: 2, z: 0 }, 0.5, 4);
  assert.equal(cur.x, 1);
  stepToward(cur, { x: 100, z: 100 }, 0.5, 4);
  assert.deepEqual(cur, { x: 100, z: 100 });
});
