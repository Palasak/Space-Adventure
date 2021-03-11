import pygame

def Game:
    def __init__(self):
        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.lives = 3
        self.money = 0

    def run(self):
        run = True
        
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()