from typing import Tuple

import pygame


class Paddle:
    """ Rectangular object that allows you to hit the ball """

    def __init__(self, left: int, top: int, width: int, height: int, speed: int, color: Tuple[int, int, int],
                 screen: pygame.Surface):
        self._rect = pygame.Rect(left, top, width, height)
        self._speed = speed
        self._color = color
        self._screen = screen

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    def up(self):
        if self._rect.top > 0:
            self._rect = self._rect.move(0, -self._speed)

    def down(self):
        if self._rect.bottom < self._screen.get_size()[1]:
            self._rect = self._rect.move(0, self._speed)

    def draw(self):
        pygame.draw.rect(self._screen, self._color, self._rect)

    def change_color(self, color):
        self._color = color