import pygame, os, random, time
from Player.player import Player
from Enemies.enemy import Enemy

WIDTH = 640
HEIGHT = 480
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Space Adventure!")

all_sprites = pygame.sprite.Group()
enemys = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    e = Enemy()
    all_sprites.add(e)
    enemys.add(e)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(FPS)

            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw()

    def draw(self):
        # Update
        all_sprites.update()

        # Draw / Render
        self.screen.fill(BLACK)
        all_sprites.draw(self.screen)

        # *after* drawing everything, flip the screen
        pygame.display.flip()


if __name__ == "__main__":
    g = Game()
    g.run()