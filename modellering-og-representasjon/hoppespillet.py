import pygame as pg

pg.init()
vindu = pg.display.set_mode((500,500))

class Spiller:
    def __init__(self):
        _y = 0
        _x = 0
        _bredde = 0
        _hoyde = 0
        _fart = 0

class Hinder:
    def __init__(self):
        _y = 0
        _x = 0
        _bredde = 0
        _hoyde = 0
        _fart = 0

class verden:
    def __init__(self):
        _alle_hindre = []
        _spiller = spiller1
        _score = 0

spiller1 = Spiller()


pg.display.flip()

pg.quit()