import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Live Wallpaper using Py")

# Set up the clock
clock = pygame.time.Clock()

# Set up the circles
num_circles = 500
circles = []
for i in range(num_circles):
    color = (random.randint(0, 255), random.randint(0,
                                                    255), random.randint(0, 255))
    x = random.randint(0, width)
    y = random.randint(0, height)
    radius = random.randint(10, 50)
    speed = random.randint(1, 5)
    dx = speed
    dy = speed
    circles.append((color, x, y, radius, dx, dy))

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update circles
    for i in range(num_circles):
        color, x, y, radius, dx, dy = circles[i]
        x += dx
        y += dy
        if x < 0 or x > width:
            dx = -dx
        if y < 0 or y > height:
            dy = -dy
        circles[i] = (color, x, y, radius, dx, dy)

    # Draw circles
    screen.fill((255, 255, 255))
    for color, x, y, radius, _, _ in circles:
        pygame.draw.circle(screen, color, (x, y), radius)

    # Update screen
    pygame.display.update()

    # Limit framerate
    clock.tick(60)
