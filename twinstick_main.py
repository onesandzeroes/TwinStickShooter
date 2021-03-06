#! /usr/bin/env python3
import pygame
from pygame.locals import *

PLAYER_KEYS = {
    'shootup': K_UP,
    'shootdown': K_DOWN,
    'shootleft': K_LEFT,
    'shootright': K_RIGHT
    'moveup': K_w,
    'movedown': K_s,
    'moveright': K_d,
    'moveleft': K_a
}


class Player:
    def __init__(self, pos, hp=5):
        self.moving = False
        self.hp = hp
        self.pos = pos

    def draw(self):
        pass

class Main:
    def __init__(self, xsize, ysize):
        pygame.init()
        self.screen = pygame.display.set_mode((xsize, ysize))
        self.player_spawn(xsize / 2, ysize / 2)
        # More stuff
        self.main_loop()
    def main_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:

    def player_spawn(self, x, y):
        self.player = Player( (x, y) )


