from typing import List, Tuple

import pygame.event

from src.paddle import Paddle


class Match:
    # TODO: Add paddles, display function and update function.

    def __init__(self, screen: pygame.Surface, paddle_size: Tuple[int, int] = (50, 100), margin_to_border: int = 30,
                 screen_color: Tuple[int, int, int] = (132, 45, 76)):
        self._screen = screen
        self._left_paddle = Paddle(left=margin_to_border, top=int(screen.get_size()[1] / 2 - paddle_size[1] / 2),
                                   width=paddle_size[0], height=paddle_size[1], color=(0, 0, 0), speed=8, screen=screen)
        self._right_paddle = Paddle(left=screen.get_size()[0] - margin_to_border - paddle_size[0],
                                    top=int(screen.get_size()[1] / 2 - paddle_size[1] / 2), width=paddle_size[0],
                                    height=paddle_size[1], color=(255, 255, 255), speed=8, screen=screen)
        self._screen_color = screen_color

    def update(self, events: List[pygame.event.Event]):
        """ Updates the state with the given events """
        for event in events:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self._left_paddle.up()
            if keys[pygame.K_s]:
                self._left_paddle.down()
            if keys[pygame.K_n]:
                self._right_paddle.up()
            if keys[pygame.K_m]:
                self._right_paddle.down()

    def display(self):
        """ Displays the current match """
        self._screen.fill(self._screen_color)
        self._left_paddle.draw()
        self._right_paddle.draw()
