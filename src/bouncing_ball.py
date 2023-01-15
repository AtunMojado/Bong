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
    margin_to_border = 30
    paddle_size = (50, 100)

    screen_saver = ScreenSaver(screen=screen)
    paddle_left = Paddle(left=margin_to_border, top=int(size[1] / 2 - paddle_size[1] / 2), width=paddle_size[0], height=paddle_size[1], color=(0, 0, 0), speed=8, screen=screen)
    paddle_right = Paddle(left=size[0] - margin_to_border - paddle_size[0], top=int(size[1]/ 2 - paddle_size[1] / 2), width=paddle_size[0], height=paddle_size[1], color=(255, 255, 255), speed=8, screen=screen)
    while True:
        events = pygame.event.get()
        screen_saver.update(events)
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_w]:
                paddle_left.up()
            if pygame.key.get_pressed()[pygame.K_s]:
                paddle_left.down()
        if screen_saver.active():
            screen_saver.display()
        else:
            screen.fill(GRAY)
            paddle_left.draw()
            paddle_right.draw()
        pygame.display.flip()
        time.sleep(0.05)
