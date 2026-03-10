import pygame
from random import randint
from uses.use import SCREEN, SIZE
from uses.background import SQUARE_SIZE

RED = (255, 0, 0)
APPLE_SIZE = SQUARE_SIZE // 2

class Apple:
    def __init__(self):
        self._collided = False
        self._pos = [0, 0]
        self._size = APPLE_SIZE

    def draw_apple(self):
        if not self._collided:
            self._pos[0] = randint(3, SIZE[0] // APPLE_SIZE - 3) * APPLE_SIZE
            self._pos[1] = randint(3, SIZE[1] // APPLE_SIZE - 3) * APPLE_SIZE
            self._collided = True


        apple_rect = pygame.Rect(self._pos[0], self._pos[1], APPLE_SIZE, APPLE_SIZE)
        pygame.draw.rect(SCREEN, RED, apple_rect)

    def change_collision(self):
        if self._collided:
            self._collided = False
        else:
            self._collided = True


    @property
    def position(self):
        return self._pos

    @property
    def size(self):
        return self._size
