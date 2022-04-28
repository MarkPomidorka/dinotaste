import pygame
import os
import random
class  Cactus(pygame.sprite.Sprite):


        def __init__(self):
            super().__init__()

            images = ['tank.png','largecake.png','largecactus2(1).png','largecactus3(1).png','smallcactus1(1).png','smallcactus2(1).png','smallcactus3(1).png']


            image = os.path.join(r'assets/images',  random.choice(images))



            self.image = pygame.image.load(image)

            self.scale = 0.7
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * self.scale, self.image.get_height() * self.scale ))

            self.rect = self.image.get_rect()
            surface = pygame.display.get_surface()
            self.rect.bottomleft = (surface.get_width() * 2, surface.get_height() / 1.95)


        def draw(self, surface):
            surface.blit(self.image, self.rect)

        def update(self):
            self.rect.x -= 5
            if self.rect.x < -50:
                self.kill()