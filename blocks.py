import pygame as pg

BL_WIDTH = 32
BL_HEIGHT = 32
BL_COLOR = (180, 100, 70)

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((BL_WIDTH, BL_HEIGHT))
        self.image.fill(BL_COLOR)
        self.rect = pg.Rect(x, y, BL_WIDTH, BL_HEIGHT)