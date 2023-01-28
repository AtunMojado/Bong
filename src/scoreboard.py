import pygame
from typing import Tuple


class ScoreBoard:


    def __init__(self, left: int, top: int, width: int, height: int,
                 result: int, color: Tuple[int, int, int], screen: pygame.Surface):

        self._rect = pygame.Rect(left, top, width, height)
        self._result = result
        self._color = color
        self._screen = screen

    def counter(self):
        pass

    def draw(self):
        pygame.draw.rect(self._screen, self._color, self._rect)