import pygame

# Draw the map

pygame.init()

WIDTH, HEIGHT = 1920, 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

screen.fill(BLACK)
pygame.draw.circle(screen, RED, (100, 100), 20)
pygame.draw.circle(screen, YELLOW, (100, 100), 20, 2)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
