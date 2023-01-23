from typing import Tuple, List
import pygame



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

    def move(self):
        self._center = (self._center[0] + self._speed[0], self._center[1] + self._speed[1])














