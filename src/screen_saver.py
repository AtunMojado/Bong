import time
from typing import List

import pygame


SCREEN_SAVER_COLOR = (0, 0, 0)


class ScreenSaver:

    def __init__(self, screen: pygame.Surface, speed: List[int] = None, counter_interval: int = 3):
        self._counter = time.time()
        self._screen = screen
        self._speed = speed if speed is not None else [8, 8]
        self._counter_interval = counter_interval
        self._ball_image = pygame.image.load("../res/intro_ball.gif")
        self._ball_rect = self._ball_image.get_rect()

    def update(self, events: List[pygame.event.Event]):
        if len(events) > 0:
            self._counter = time.time()

    def active(self) -> bool:
        return time.time() - self._counter > self._counter_interval

    def display(self):
        self._screen.fill(SCREEN_SAVER_COLOR)
        if self._ball_rect.right > self._screen.get_size()[0]:
            self._speed[0] = -self._speed[0]
        if self._ball_rect.left < 0:
            self._speed[0] = -self._speed[0]
        if self._ball_rect.top < 0:
            self._speed[1] = -self._speed[1]
        if self._ball_rect.bottom > self._screen.get_size()[1]:
            self._speed[1] = -self._speed[1]
        self._ball_rect = self._ball_rect.move(self._speed)
        self._screen.blit(self._ball_image, self._ball_rect)
