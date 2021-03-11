import pygame

GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.WIDTH = 640
        self.HEIGHT = 480
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.WIDTH / 2
        self.rect.bottom = self.HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0