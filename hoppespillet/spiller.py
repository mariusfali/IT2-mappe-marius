import pygame as pg

class Spiller:
    def __init__(self):
        self._x = 20
        self._y = 20

    def tegn(self, vindu):
        pg.draw.circle(vindu, (130,70,50), (self._x, self._y), 25)