from typing import Tuple, List
import pygame



class Ball:

    def __init__(self, screen: pygame.Surface, color: Tuple[int, int, int], center: Tuple[int, int], radius: int, speed: Tuple[int, int]):
        """Circle that goes all over the screen and collides with the paddles or score goals"""
        self._screen = screen
        self._speed = speed
        self._color = color
        self._radius = radius
        self._center = center


    def draw(self):
        pygame.draw.circle(self._screen, self._color, self._center, self._radius)

    def movement(self):
        speed = self._speed
        ball = pygame.draw.circle(self._screen, self._color, self._center, self._radius)














