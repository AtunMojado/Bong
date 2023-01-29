import pygame
from typing import Tuple

from pygame.font import Font

from src.ball import Ball




class ScoreBoard:


    def __init__(self, left: int, top: int, width: int, height: int,
                 color: Tuple[int, int, int], screen: pygame.Surface):

        self._rect = pygame.Rect(left, top, width, height)
        self._color = color
        self._screen = screen
        self._font: Font = pygame.freetype.SysFont('arialunicode', 30)
        self._left_counter = 0

    def set_left_counter(self, number: int):
        self._left_counter = number

    def draw(self):
        #pygame.draw.rect(self._screen, self._color, self._rect)

        #right scoreboard

        font = pygame.font.SysFont('geneva', 40)
        text = font.render('0', True, 'black', 'yellow')
        text_rect = text.get_rect()
        text_rect.center = (self._screen.get_size()[0] / 2 - 25, self._screen.get_size()[1] / 2 - 150)

        #left scoreboard

        font_2 = pygame.font.SysFont('geneva', 40)
        text_2 = font_2.render('0', True, 'black', 'red')
        text_rect_2 = text_2.get_rect()
        text_rect_2.center = (self._screen.get_size()[0] / 2 + 25, self._screen.get_size()[1] / 2 - 150)


        self._screen.blit(text, text_rect)
        self._screen.blit(text_2, text_rect_2)
















