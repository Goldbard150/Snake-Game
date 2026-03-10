import pygame
from random import randint
from uses.use import SCREEN, SIZE
from uses.background import SQUARE_SIZE

RED = (255, 0, 0)
APPLE_SIZE = SQUARE_SIZE

class Apple:
    def __init__(self):
        self._image = pygame.image.load("assets/Apple.png")
        self._image = pygame.transform.scale(self._image, (APPLE_SIZE, APPLE_SIZE))
        self._rect = self._image.get_rect()
        self._rect.topleft = (100, 100)
        self._collided = False

    def draw_apple(self):
        if not self._collided:
            x = randint(3, SIZE[0] // APPLE_SIZE - 3) * APPLE_SIZE
            y = randint(3, SIZE[1] // APPLE_SIZE - 3) * APPLE_SIZE
            self._rect.topleft = (x, y)
            self._collided = True


        SCREEN.blit(self._image, self._rect)

    def change_collision(self):
        if self._collided:
            self._collided = False
        else:
            self._collided = True


    @property
    def position(self):
        return self._rect.topleft

    @property
    def size(self):
        return APPLE_SIZE

    @property
    def rect(self):
        return self._rect
