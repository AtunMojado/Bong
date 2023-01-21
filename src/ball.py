from typing import Tuple, List
import pygame


class Ball:

    def __init__(self, color: Tuple[int, int, int], center: Tuple[int, int], radius: int, speed: int, screen: pygame.Surface):
        """Circle that goes all over the screen and collides with the paddles or score goals"""
        self._screen = screen
        self._speed = speed
        self._color = color
        self._radius = radius
        self._center = center

    def draw(self):
        pygame.draw.circle(self._screen, self._color, self._center, self._radius)

    def change_color(self, color):
        self._color = color

    #def movement(self):
        #if self._ball.top > 0:
            #self._ball.move(0, -self._speed)
        #if self._ball.bottom < self._screen.get_size()[1]:
            #self._ball = self._ball.move(0, self._speed)