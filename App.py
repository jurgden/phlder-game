import pygame

# initialize pygame
pygame.init()

screen = pygame.display.set_mode((1080, 720))

# Title and Icon
pygame.display.set_caption("Mikets Basement")
icon = pygame.image.load('mikes.png')
pygame.display.set_icon(icon)

# This is our game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Our RGB values HEX:#050505
    screen.fill((5, 5, 5))
    pygame.display.update()
