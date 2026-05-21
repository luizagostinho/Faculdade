import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        self.menu = Menu(self.window)

    def run(self,):
        self.menu.run()

        pygame.quit()