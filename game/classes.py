from random import uniform

import pygame


class GameObject:
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.h, self.w)


class MoveableGameObject(GameObject):
    def __init__(self, x, y, h, w):
        GameObject.__init__(self, x, y, h, w)
        self.xv = 0
        self.yv = 0

    def pos_update(self):
        self.x += self.xv
        self.y += self.yv
        if self.x >= 800:
            self.xv = uniform(-.01, -7)
        if self.y >= 600:
            self.yv = uniform(-.01, -7)
        if self.x <= 0:
            self.xv = uniform(.01, 7)
        if self.y <= 0:
            self.yv = uniform(.01, 7)


class CharacterObject(MoveableGameObject):
    def __init__(self, x, y, h, w):
        MoveableGameObject.__init__(self, x, y, h, w)
        self.jf = 5
        self.jh = 20
        self.onGround = False

        # def jump(self):


player = MoveableGameObject(0, 3, 2, 2)
ground = MoveableGameObject(0, 0, 2, 2)

print(player.get_rect().colliderect(ground.get_rect()))
