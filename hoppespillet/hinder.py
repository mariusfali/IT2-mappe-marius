import pygame as pg
from random import randint
class Hinder:
    def __init__(self):
        self._x = 300
        self._hoyde = randint(20,100)
        self._y = 500 - self._hoyde
        self._bredde = 10

    def tegn(self, vindu):
        pg.draw.rect(vindu, (190,50,80), (self._x,self._y,self._bredde,self._hoyde))

    def flytt_venstre(self):
        self._x -= 1