import sys
import time

import pygame

from src.match import Match
from src.screen_saver import ScreenSaver


def bounce():
    pygame.init()
    size = (700, 400)
    screen = pygame.display.set_mode(size)
    screen_saver = ScreenSaver(screen=screen)
    match = Match(screen=screen)

    while True:
        events = pygame.event.get()
        match.update(events)
        screen_saver.update(events)
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
        if screen_saver.active():
            screen_saver.display()
        match.display()
        pygame.display.flip()
        time.sleep(0.05)
