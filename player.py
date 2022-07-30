import re
import pygame as pg

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = (100, 20, 0)
JUMP_POWER = 10
GRAVITY = 0.35

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.onGround = False
        self.yvel = 0
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = pg.Surface((WIDTH, HEIGHT))
        self.image.fill(COLOR)
        self.rect = pg.Rect(x, y, WIDTH, HEIGHT)

    def update(self, screen, left, right, up):
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
        if left:
            self.xvel = -MOVE_SPEED
        if right:
            self.xvel = MOVE_SPEED
        if not(left or right):
            self.xvel = 0
        if not self.onGround:
            self.yvel += GRAVITY
        
        self.onGround = False
        self.rect.y += self.yvel
        self.rect.x += self.xvel
        screen.blit(self.image, (self.rect.x, self.rect.y))
