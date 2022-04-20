import pygame

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image_run1 = pygame.image.load(r"assets\images\dinorun1.png")
        self.image_run2 = pygame.image.load(r"assets\images\dinorun2.png")

        self.image = self.image_run1
        self.rect = self.image.get_rect()

        self.step = 0

        self.jumping = False

    def jump(self):


    def update(self):

        self.step += 1
        if self.step % 7 == 0:
            if self.image == self.image_run1:
                self.image = self.image_run2
            else:
                self.image = self.image_run1
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.jumping = True

        if self.jumping:
            self.jump()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


