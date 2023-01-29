import pygame
from typing import Tuple
from src.ball import Ball




class ScoreBoard:


    def __init__(self, left: int, top: int, width: int, height: int,
                 color: Tuple[int, int, int], screen: pygame.Surface):

        self._rect = pygame.Rect(left, top, width, height)
        self._color = color
        self._screen = screen
        self._ball = Ball
        self._font = pygame.freetype.SysFont('Arial', 30)
       

    @property
    def rect(self) -> pygame.Rect:
        return self._rect
    def draw(self):
        pygame.draw.rect(self._screen, self._color, self._rect)


    def count(self):
        #font = pygame.font.SysFont('chalkduster.ttf', 72)
        left_scoreboard = self._font.render('0', True, (0, 0, 0))











