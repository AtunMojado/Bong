from typing import Tuple, List
import pygame

from src.paddle import Paddle
from src.scoreboard import ScoreBoard



class Ball:

    def __init__(self, center: Tuple[int, int], radius: int, speed: Tuple[int, int], color: Tuple[int, int, int],
                 screen: pygame.Surface):
        """Circle that goes all over the screen and collides with the paddles or score goals"""
        self._center = center
        self._radius = radius
        self._speed = speed
        self._color = color
        self._screen = screen


    def draw(self):
        pygame.draw.circle(self._screen, self._color, self._center, self._radius)

    def move(self, left_paddle: Paddle, right_paddle: Paddle):
        """
        Function to move the ball taking into consideration the collisions with the given paddles.
        :param left_paddle: Paddle on the lef side of the screen
        :param right_paddle: Paddle on the right side of the screen
        :return:
        """
        self._center = (self._center[0] + self._speed[0], self._center[1] + self._speed[1])
        self.wall_collision()
        self.paddle_collision(left_paddle, right_paddle)

    def wall_collision(self):
        #bottom wall
        if self._center[1] + self._radius > self._screen.get_size()[1]:
            self._speed = (self._speed[0], -abs(self._speed[1]))

        #top wall
        if self._center[1] - self._radius < 0:
            self._speed = (self._speed[0], abs(self._speed[1]))

    def paddle_collision(self, left_paddle: Paddle, right_paddle: Paddle):
        #collisions for left paddle
        if self._center[0] - self._radius < left_paddle.rect.right and left_paddle.rect.top < self._center[1] < left_paddle.rect.bottom:
            self._speed = (abs(self._speed[0]), self._speed[1])

        #collisions for right paddle
        if self._center[0] + self._radius > right_paddle.rect.left and right_paddle.rect.top < self._center[1] < right_paddle.rect.bottom:
            self._speed = (-abs(self._speed[0]), self._speed[1])

    def goal_left(self, set_left_counter: ScoreBoard):
        if self._center[0] + self._radius < 0:
            set_left_counter += 1





    def change_color(self, color):
        self._color = color





























