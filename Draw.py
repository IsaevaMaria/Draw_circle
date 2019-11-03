import pygame
from random import choice, randint

pygame.init()
size = width, heigth = 400, 300
screen = pygame.display.set_mode(size)
screen2 = pygame.Surface(screen.get_size())
pygame.display.set_caption("Balls Animation")
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
screen2.fill((255, 255, 255))
fps = 20
speed = 100
radius = 10


def draw(x, y, color):
    pygame.draw.circle(screen, color, (x, y), radius)


def run(x_start, y_start):
    x = x_start
    y = y_start
    c = (choice(range(255)), choice(range(255)), choice(range(255)))
    draw(x, y, c)
    while y < heigth - 2 * radius:
        screen.fill((255, 255, 255))
        screen.blit(screen2, (0, 0))
        y += speed // fps
        draw(x, y, c)
        pygame.display.flip()
        clock.tick(fps)
    screen2.blit(screen, (0, 0))


running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x_start = ev.pos[0]
            y_start = ev.pos[1]
            run(x_start, y_start)
    pygame.display.flip()
    clock.tick(20)
pygame.quit()