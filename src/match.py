from typing import List, Tuple

import pygame
import pygame.event
from pygame.event import Event

from src.paddle import Paddle
from src.ball import Ball
from src.scoreboard import ScoreBoard





class Match:



    def __init__(self, screen: pygame.Surface, scoreboard_size: Tuple[int, int] = (70, 60),
                 paddle_size: Tuple[int, int] = (30, 100),
                 margin_to_top: int = 20, margin_to_border: int = 25,
                 screen_color: Tuple[int, int, int] = (176, 224, 230), ball_position: Tuple[int, int] = (350, 200),
                 ball_speed: Tuple[int, int] = (10, 10)):

        self._screen = screen

        self._left_paddle = Paddle(left=margin_to_border, top=int(screen.get_size()[1] / 2 - paddle_size[1] / 2),
                                   width=paddle_size[0], height=paddle_size[1], color=(0, 0, 0), speed=8, screen=screen)

        self._right_paddle = Paddle(left=screen.get_size()[0] - margin_to_border - paddle_size[0],
                                    top=int(screen.get_size()[1] / 2 - paddle_size[1] / 2), width=paddle_size[0],
                                    height=paddle_size[1], color=(70, 70, 70), speed=8, screen=screen)

        self._ball = Ball(color=(0, 15, 150), radius=11, center= ball_position, speed= ball_speed, screen=screen)

        self._right_scoreboard = ScoreBoard(left= int(screen.get_size()[0]/2), top= margin_to_top,
                                            width= scoreboard_size[0], height= scoreboard_size[1],
                                            result= int, color=(255, 0, 0), screen=screen)

        self._left_scoreboard = ScoreBoard(left= int(screen.get_size()[0]/2 - scoreboard_size[0]),
                                            top= margin_to_top, width= scoreboard_size[0], height= scoreboard_size[1],
                                           result= int, color=(255, 255, 0), screen=screen)

        self._screen_color = screen_color

        self._running = False  #to define ball is in screen center before game begins




    def update(self, events: List[Event]):
        """ Updates the state with the given events """

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self._running = True

        if self._running == True:
            self._ball.move(self._left_paddle, self._right_paddle)

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
        self._ball.draw()
        self._left_scoreboard.draw()
        self._right_scoreboard.draw()


