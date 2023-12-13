"""
2D simulator for any object that can be represented as a circle
"""
import pygame

class Simulator:
    """
    Simulator for any object that can be represented as a circle
    """

    def __init__(
            self, 
            width=1280, 
            height=720, 
            dt=0.01
            ):
        """
        Initialize the simulator
        """
        self.width = width
        self.height = height
        self.dt = dt
        self.objects = []
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.background_color = "blue"
        self.screen.fill(self.background_color)
        self.clock = pygame.time.Clock()
        self.running = True
        self.time = 0

    def add_dynamic_obj(self, obj):
        """
        Add a dynamic object to the simulation
        """
        self.objects.append(obj)

    def run(self):
        """
        Run the simulation
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(self.background_color)

            for obj in self.objects:
                obj.update(self.dt)
                obj.draw(self.screen)

            # create a text message on the screen to display the current time
            time_font = pygame.font.Font(None, 16)   # default font, size 36 pt
            time_text = time_font.render(f"{self.time}", True, "white")
            time_text_rect = time_text.get_rect()
            time_text_rect.center = (self.width / 2, 20)
            self.screen.blit(time_text, time_text_rect)
            
            # flip() the display to put your work on screen
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
            self.time += self.dt

        pygame.quit()

class wasd_circle:
    """
    A circle controlled by WASD
    """

    def __init__(
            self, 
            pos, 
            radius=40, 
            color="orange", 
            speed=300
            ):
        """
        Initialize the circle
        """
        self.pos = pos
        self.radius = radius
        self.color = color
        self.speed = speed

    def update(self, dt):
        """
        Update the circle
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.pos.y += self.speed * dt
        if keys[pygame.K_a]:
            self.pos.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.pos.x += self.speed * dt

    def draw(self, screen):
        """
        Draw the circle
        """
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

# To run the simulator
sim = Simulator()
sim.add_dynamic_obj(wasd_circle(pygame.Vector2(sim.width / 2, sim.height / 2)))
sim.run()
