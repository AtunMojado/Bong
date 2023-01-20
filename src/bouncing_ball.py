import sys
import time

import pygame

from src.paddle import Paddle
from src.screen_saver import ScreenSaver


def bounce():
    pygame.init()
    size = (700, 400)
    GRAY = (110, 110, 110)
    screen = pygame.display.set_mode(size)
    screen_saver = ScreenSaver(screen=screen)
    while True:
        events = pygame.event.get()
        screen_saver.update(events)
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
        if screen_saver.active():
            screen_saver.display()
        else:
            screen.fill(GRAY)
        pygame.display.flip()
        time.sleep(0.05)
