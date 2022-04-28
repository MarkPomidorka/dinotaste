import pygame
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()

        self.image_run1 = pygame.image.load(r"assets\images\dinorun1.png")
        self.image_run2 = pygame.image.load(r"assets\images\dinorun2.png")
        self.sound_jump = pygame.mixer.Sound(r"assets\sounds\jump.wav")
        self.sound_die = pygame.mixer.Sound(r"assets\sounds\die.wav")

        self.image = self.image_run1
        self.rect = self.image.get_rect()

        self.rect.x = 15
        self.rect.y = 200
        self.step = 0

        self.jumping = False
        self.height = 15

    def draw(self, surface):
       surface.blit(self.image, self.rect)

    def jump(self):
        self.rect.y -= self.height
        self.height -= 1
        if self.height < -15:
            self.height = 15
            self.jumping = False

    def update(self):

        self.step += 1
        if self.step % 7 == 0:
            if self.image == self.image_run1:
                self.image = self.image_run2
            else:
                self.image = self.image_run1


        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if not self.jumping:
                self.jumping = True
                #self.sound_jump.play()

        if self.jumping:
            self.jump()



