"""
Minimal pygame renderer. Deliberately simple for Phase 1 -- swap for something
richer once the sim logic is validated.
"""
import pygame

BIOME_COLORS = {
    0: (120, 170, 80),   # plains - green
    1: (60, 120, 200),   # river - blue
    2: (130, 130, 130),  # mountain - gray
    3: (210, 180, 100),  # desert - tan
    4: (70, 60, 60),     # cave - dark brown
}

AGENT_COLOR = (230, 30, 30)


class Renderer:
    def __init__(self, world_size: int, cell_px: int = 6):
        self.world_size = world_size
        self.cell_px = cell_px
        self.screen_size = world_size * cell_px
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        pygame.display.set_caption("CogniWorld")
        self.font = pygame.font.SysFont(None, 20)

    def draw(self, world, agents, step: int, alive_count: int):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        biome_grid = world.biome_name_grid()
        for y in range(self.world_size):
            for x in range(self.world_size):
                color = BIOME_COLORS[int(biome_grid[y, x])]
                rect = (x * self.cell_px, y * self.cell_px, self.cell_px, self.cell_px)
                self.screen.fill(color, rect)

        positions = agents.pos[agents.alive].cpu().numpy()
        for x, y in positions:
            rect = (int(x) * self.cell_px, int(y) * self.cell_px, self.cell_px, self.cell_px)
            self.screen.fill(AGENT_COLOR, rect)

        label = self.font.render(f"step {step}  alive {alive_count}", True, (255, 255, 255))
        self.screen.blit(label, (5, 5))

        pygame.display.flip()
        return True

    def close(self):
        pygame.quit()
