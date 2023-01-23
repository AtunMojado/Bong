from typing import Tuple, List
import pygame

from src.paddle import Paddle


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
        self._center = (self._center[0] + self._speed[0], self._center[1] + self._speed[1])
        self.wall_collision()
        self.paddle_collision()


    def wall_collision(self):
        if self._center[1] + self._radius > self._screen.get_size()[1]:
            self._speed = (self._speed[0], -self._speed[1])
        if self._center[0] + self._radius > self._screen.get_size()[0]:
            self._speed = (-self._speed[0], self._speed[1])
        if self._center[1] - self._radius < 0:
            self._speed = (self._speed[0], -self._speed[1])
        if self._center[0] - self._radius < 0:
            self._speed = (-self._speed[0], self._speed[1])
    def paddle_collision(self):
        pass
















