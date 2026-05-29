#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
from code.const import ENTITY_SPEED
from code.enemyShot import EnemyShot


class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shot(self):
        if self.shot_delay > 0:
            self.shot_delay -= 1
        return EnemyShot(name=f'{self.name}Shot',position=(self.rect.centerx, self.rect.centery))
