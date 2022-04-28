import sys
import pygame
from sprites.road import Road
from sprites.cloud import Cloud
from sprites.dino import Dino
from sprites.cactus import Cactus
from sprites.game import Score
from sprites.game import GameOver

player = Dino()

pygame.init()

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
cactus = pygame.sprite.Group()
score = Score()

running = True


def main():
    # Спрайты
    road = Road()
    clouds = pygame.sprite.Group()
    cactus = pygame.sprite.Group()
    score = Score()

    game_over = False
    running = True



    while running:

        # Частота обновления экрана
        clock.tick(FPS)

        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    main()

        for cact in cactus:
            if pygame.sprite.collide_mask(player, cact) and not game_over:
                player.sound_die.play()
                end = GameOver()
                game_over = True




        # Рендеринг
        screen.fill((255, 255, 255))
        road.draw(screen)
        clouds.draw(screen)
        player.draw(screen)
        cactus.draw(screen)
        score.draw(screen)
        if game_over:
            end.draw(screen)

        # update sprites
        if not game_over:
            road.update()
            clouds.update()
            player.update()
            cactus.update()
            score.update()

            if len(clouds)<3:
                cloud = Cloud()
                clouds.add(cloud)

            if len(cactus) < 1:
                cact = Cactus()
                cactus.add(cact)

        # screen update
        pygame.display.update()

if __name__ == "__main__":
    main()