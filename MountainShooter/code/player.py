#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
import pygame


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= 2

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_DOWN] and self.rect.bottom > 0:
            self.rect.centery -= -2

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= 2

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT] and self.rect.right > 0:
            self.rect.centerx -= -2

