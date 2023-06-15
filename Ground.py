import pygame as pg

from Player import *

class Ground:
    def __init__(self, x, y, width, height, color):
        self.rect = pg.Rect(x, y, width, height)
        self.color = color
        self.tag = "ground"

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)