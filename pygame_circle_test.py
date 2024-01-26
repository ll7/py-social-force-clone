# <https://www.pygame.org/docs/#quick-start>
# Example file showing a circle moving on screen
import pygame
import numpy as np

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
second_circle_pos = pygame.Vector2(screen.get_width() / 2 + 100, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Calculate the direction from the first circle to the second
    direction = second_circle_pos - player_pos

    # Calculate the distance between the two circles
    distance = direction.length()

    # Normalize the direction vector (to have a length of 1)
    direction_normalized = direction.normalize()

    
    print("distance: ", distance)
    if distance > 100:
        scale_factor = 0.0
    elif distance == 0.0:
        scale_factor = 0.0
    else:
        scale_factor = 100.0 / distance

    # Move the second circle in the opposite direction
    second_circle_pos += direction_normalized * scale_factor

    # Draw the first circle
    pygame.draw.circle(screen, "blue", (int(player_pos.x), int(player_pos.y)), 50)

    # Draw the second circle
    pygame.draw.circle(screen, "red", (int(second_circle_pos.x), int(second_circle_pos.y)), 50)


    # pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()