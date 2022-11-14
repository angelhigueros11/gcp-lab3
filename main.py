# Angel Higueros - 20460
# Lab 3 - Game of Life

import itertools
from random import *
from pygame import *
from utils import *


class GameOfLife(object):
    def __init__(self):
        self.framebuffer = None
        self.current_color = (255, 0, 0)

    def create_windows(self, width, height):

        self.framebuffer = display.set_mode((width, height))

        semillas = [[randint(10, 400), randint(10, 400)] for _ in range(6000)]

        for j in semillas:
            self.glColor((255, 0, 0))
            self.point((j[0], j[1]))

    def create_word(self):
        self.celula = self.framebuffer.copy()

    def point(self, cords):
        self.framebuffer.set_at(
            cords,
            self.current_color
        )

    def glColor(self, color):
        self.current_color = color

    def play(self, x, y):
        indexX = x - 1
        indexY = y - 1
        direction = 0
        cord = self.celula.get_at((x, y))
        contador = 0

        index = [x - 1, y - 1]
        if cord[:3] == (255, 0, 0):
            while (contador <= 2):
                indexX = x - 1

                for _ in range(3):
                    cords = self.celula.get_at(
                        (indexX, indexY)
                    )
                    pix_color = cords[:3]
                    if pix_color == (255, 0, 0):
                        index = [indexX, indexY]

                        if index != [x, y]:
                            direction += 1

                    indexX += 1

                contador += 1
                indexY = indexY + 1

            return direction

        elif cord[:3] == (0, 0, 0):
            while contador <= 2:
                indexX = x - 1

                for _ in range(3):
                    cords = self.celula.get_at(
                        (indexX, indexY)
                    )
                    if cords == (255, 0, 0)[:3]:
                        direction += 1

                    indexX = indexX + 1

                contador += 1
                indexY += 1

            return direction

    def clear(self):
        self.framebuffer.fill((0, 0, 0))

    def load(self):
        for y, x in itertools.product(range(10, 400), range(10, 400)):
            rand = self.play(x, y)
            cords = self.celula.get_at((x, y))
            get_celula = cords[:3]

            # Avanzar
            if rand == 3:
                self.glColor((255, 0, 0))
                self.point((x, y))

            # Reglas de vida
            elif get_celula == (255, 0, 0) and rand < 2:
                self.glColor((0, 0, 0))
                self.point((x, y))

            elif get_celula == (255, 0, 0) and rand in [2, 3]:
                self.glColor((255, 0, 0))
                self.point((x, y))

            elif get_celula == (255, 0, 0) and rand > 3:
                self.glColor((0, 0, 0))
                self.point((x, y))


# IMPLEMENTACION
init()
r = GameOfLife()
r.create_windows(450, 450)

while True:
    r.create_word()
    r.clear()
    r.load()
    display.flip()
