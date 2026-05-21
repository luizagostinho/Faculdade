import pygame

from code.Const import MENU_OPTION
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        self.menu = Menu(self.window)

    def run(self,):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                pass
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
        self.menu.run()

        pygame.quit()