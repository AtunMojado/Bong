import pygame
from typing import Tuple

class Button():
    def __init__(self, screen: pygame.Surface, color: Tuple[int, int, int], left: int, top: int, width: int, height: int):
        self._rect = pygame.Rect(left, top, width, height)
        self._screen = screen
        self._color = color
    def draw(self):
        pygame.draw.rect(self._screen, self._color, self._rect)
    def click(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self._rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                action = True
        return action