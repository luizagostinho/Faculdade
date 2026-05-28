#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
from  code.const import WIN_WIDTH, ENTITY_SPEED


class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
