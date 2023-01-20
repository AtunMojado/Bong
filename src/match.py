from typing import List

import pygame.event

from src.paddle import Paddle


class Match:
    # TODO: Add paddles, display function and update function.

    def __int__(self, screen: pygame.Surface, paddle_size=(50, 100), margin_to_border=30):
        self._left_paddle = Paddle(left=margin_to_border, top=int(screen.get_size()[1] / 2 - paddle_size[1] / 2),
                                   width=paddle_size[0], height=paddle_size[1], color=(0, 0, 0), speed=8, screen=screen)
        self._right_paddle = Paddle(left=screen.get_size()[0] - margin_to_border - paddle_size[0],
                                    top=int(screen.get_size()[1]/ 2 - paddle_size[1] / 2), width=paddle_size[0],
                                    height=paddle_size[1], color=(255, 255, 255), speed=8, screen=screen)

    def update(self, events: List[pygame.event.Event]):
        """ Updates the state with the given events """
        pass

    def display(self):
        """ Displays the current match """
        pass

