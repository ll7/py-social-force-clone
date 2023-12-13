import pygame

class Simulator:
    """
    A class representing a game simulator.
    """
    def __init__(self, width=1280, height=720):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("purple")
            pygame.draw.circle(self.screen, "red", self.player_pos, 40)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_pos.y -= 300 * self.dt
            if keys[pygame.K_s]:
                self.player_pos.y += 300 * self.dt
            if keys[pygame.K_a]:
                self.player_pos.x -= 300 * self.dt
            if keys[pygame.K_d]:
                self.player_pos.x += 300 * self.dt

            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()

# To run the simulator
sim = Simulator()
sim.run()