import sys
import pygame
from sprites.road import Road
from sprites.cloud import Cloud
from sprites.dino import Dino

player = Dino()

pygame .init()

WIDTH = 700
HEIGHT = 500
FPS = 60

# Создание окна
screen = pygame .display.set_mode((WIDTH, HEIGHT))
pygame .display.set_caption("Dino taste")
clock = pygame .time.Clock()

# Спрайты
road = Road()
clouds = pygame.sprite.Group()
running = True
while running:
    # Частота обновления экрана
    clock.tick(FPS)

    # События/Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Рендеринг
    screen.fill((255, 255, 255))
    road.draw(screen)
    clouds.draw(screen)
    player.draw(screen)

    # update sprites
    road.update()
    clouds.update()
    player.update()

    if len(clouds)<3:
        cloud = Cloud()
        clouds.add(cloud)


    # screen update
    pygame.display.update()
