#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SHOT_DELAY, PLAYER_KEY_SHOOT
from code.const import ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from code.entity import Entity
import pygame
from code.playerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]


    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < 324:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < 576:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shot(self):

        if self.shot_delay > 0:
            self.shot_delay -= 1

        pressed_key = pygame.key.get_pressed()

        if pressed_key[PLAYER_KEY_SHOOT[self.name]] and self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]

            return PlayerShot(name=f'{self.name}Shot',position=(self.rect.centerx, self.rect.centery)
            )
