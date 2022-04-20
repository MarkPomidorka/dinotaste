import pygame
import random
class  Cloud(pygame.sprite.Sprite):


    speed = 0
    def __init__(self):
        super() .__init__()
        self.image = pygame.image.load(r"assets\images\cloud(1).png")
        #self.image1 = pygame.image.load(r"assets\images\cloud(1).png")
        self.image = pygame.transform.scale(self.image,(100,50))
        #self.image1 = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.x = surface.get_width()
        self.rect.y = random.randint(0, surface.get_height() /2 - self.rect.height)
        self.speed = random.randint(1,10)

    def draw(self, surface):
        surface.blit(self.image, self.rect)




    def update(self):
        self.rect.x -= self.speed



        if self.rect.x < -50:
            self.kill()
