import pygame
from typing import Tuple
pygame.init()
class InitFade():
    def __init__(self, screen: pygame.Surface, left: int, top: int, width: int, height: int, color: Tuple[int, int, int], speed: int):
        self._left = left
        self._top = top
        self._width = width
        self._height = height
        self._rect = pygame.Rect(self._left, self._top, self._width, self._height)
        self._color = color
        self._speed = speed
        self._screen = screen
    def draw(self):
        pygame.draw.rect(self._screen, self._color, self._rect)

    def move(self):
        if self._rect.left < self._screen.get_size()[0]:
            self._rect.left += self._speed