import pygame
from typing import Tuple

from pygame.font import Font

class ScoreBoard:
    def __init__(self, screen: pygame.Surface):

        self._screen = screen
        self._left_counter = 0
        self._right_counter = 0

    def set_left_counter(self, number: int):
        self._left_counter = number
    def set_right_counter(self, number: int):
        self._right_counter = number

    def draw(self):
        # type of letter for both scoreboards
        font = pygame.font.SysFont('geneva', 40)

        #Left scoreboard
        LEFT_SB_COLOR = (50,205,50)

        # whats printed on left scoreboard
        text_L = font.render(str(self._left_counter), True, 'black', LEFT_SB_COLOR)

        # stablish a rect behind the text to make it positional
        text_rect_L = text_L.get_rect()

        # left scoreboard screen position
        text_rect_L.center = (self._screen.get_size()[0] / 2 - 25, self._screen.get_size()[1] / 2 - 150)

        #Right scoreboard
        RIGHT_SB_COLOR = (34,139,34)

        text_R = font.render(str(self._right_counter), True, 'black', RIGHT_SB_COLOR)
        text_rect_R = text_R.get_rect()
        text_rect_R.center = (self._screen.get_size()[0] / 2 + 25, self._screen.get_size()[1] / 2 - 150)


        self._screen.blit(text_L, text_rect_L) #shows both counters in screen
        self._screen.blit(text_R, text_rect_R)


















