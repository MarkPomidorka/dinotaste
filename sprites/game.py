import pygame


class Score(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.step = 0
        self.points = 0
        self.font = pygame.font.Font(r"assets\fonts\gamefont.ttf", 20)
        self.image = self.font.render(f"High score {self.points}", True, (83, 84, 85))
        self.rect = self.image.get_rect()
        self.rect.x = 230
        self.rect.y = 30

    def draw(self, surface):

        surface.blit(self.image, self.rect)
        self.image = self.font.render(f"High score {self.points}", True, (83, 84, 85))


    def update(self):

        self.step += 1

        if self.step % 10 == 0:
            self.points += 1

class GameOver(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(r"assets\fonts\gamefont.ttf", 20)
        self.image = self.font.render(f"Game Over", True, (83, 84, 85))
        self.rect = self.image.get_rect()
        self.rect.x = 260
        self.rect.y = 100

    def draw(self, surface):

        surface.blit(self.image, self.rect)

