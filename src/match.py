import sys
from typing import List, Tuple

import pygame
import pygame.event
from pygame.event import Event

from src.paddle import Paddle
from src.ball import Ball
from src.scoreboard import ScoreBoard
from src.EndFade import EndFade

class Match:

    def __init__(self,
                 screen: pygame.Surface,
                 paddle_size: Tuple[int, int] = (20, 120),
                 margin_to_border: int = 20,
                 screen_color: Tuple[int, int, int] = (110,139,61),
                 ball_position: Tuple[int, int] = (350, 200),
                 ball_speed: Tuple[int, int] = (12, 10), left_paddle_color = (192,255,62), right_paddle_color = (124,252,0),
                 endfade_left_pos: int = 0, endfade_top_pos: int = 0, endfade_width: int = 700,
                 endfade_height: int = 0, endfade_color: Tuple[int, int, int] = (0, 0, 0), endfade_speed: int = 7):


        self._screen = screen
        self._ball_starting_position = ball_position

        self._left_paddle = Paddle(left=margin_to_border, top=int(screen.get_size()[1] / 2 - paddle_size[1] / 2),
                                   width=paddle_size[0], height=paddle_size[1], color=left_paddle_color, speed=8, screen=screen)
        self._right_paddle = Paddle(left=screen.get_size()[0] - margin_to_border - paddle_size[0],
                                    top=int(screen.get_size()[1] / 2 - paddle_size[1] / 2), width=paddle_size[0],
                                    height=paddle_size[1], color=right_paddle_color, speed=8, screen=screen)
        self._ball = Ball(color=(0, 60, 0), radius=7, position=self._ball_starting_position, speed=ball_speed, screen=screen)

        self._end_fade = EndFade(screen=self._screen, left=endfade_left_pos, top=endfade_top_pos, width=endfade_width,
                                 height=endfade_height, color=endfade_color, speed=endfade_speed)

        self._scoreboard = ScoreBoard(screen)
        self._left_counter = 0
        self._right_counter = 0

        self._screen_color = screen_color
        self._running = False
        self._screen = screen

    def update(self, events: List[Event]):
        """ Updates the state with the given events """

        keys = pygame.key.get_pressed()

        # pressing spacebar, game begins
        if keys[pygame.K_SPACE]:
            self._running = True

        if self._running == True:
            self._ball.move(self._left_paddle, self._right_paddle)

        # allows you to move the paddles pressing each keys (w,s--n,m)
        if keys[pygame.K_w]:
            self._left_paddle.up()
        if keys[pygame.K_s]:
            self._left_paddle.down()
        if keys[pygame.K_n]:
            self._right_paddle.up()
        if keys[pygame.K_m]:
            self._right_paddle.down()

        #conditions if a goal happens
        if self._ball.goal_left:
            self._right_counter += 1
            self._running = False
            self._ball_starting_position = self._ball.set_ball_position()
            self._ball.goal_left = False
            self._scoreboard.set_right_counter(number=self._right_counter)

        if self._ball.goal_right:
            self._left_counter += 1
            self._running = False
            self._ball_starting_position = self._ball.set_ball_position()
            self._ball.goal_right = False
            self._scoreboard.set_left_counter(number=self._left_counter)




    def display(self):
        """ Displays the current match """
        self._screen.fill(self._screen_color)
        self._left_paddle.draw()
        self._right_paddle.draw()
        self._ball.draw()
        self._scoreboard.draw()
        # conditions if scoreboard reaches 10points
        if self._left_counter >= 2 or self._right_counter >= 2:
            self._end_fade.draw()
            self._end_fade.move()



