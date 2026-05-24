import pygame

from code.const import MENU_OPTION
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu
from code.level import Level


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

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level 1', menu_return)
                leve_return = level.run()



            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
        self.menu.run()

        pygame.quit()