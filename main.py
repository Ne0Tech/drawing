import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
magenta = (255,0,255)
purple = (128,0,255)
blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
cyan = (0,255, 255)
orange = (255,128,0)

display_surface.fill (white)
CENTER= (300, 300)
RADIUS= 100
pygame.draw.circle(display_surface, red, CENTER, RADIUS)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()