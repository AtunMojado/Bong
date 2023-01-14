import sys
import time

import pygame

def bounce():
    pygame.init()
    size = (320, 240)
    color = 255, 255, 255
    speed = [5, 5]
    screen = pygame.display.set_mode(size)
    ball = pygame.image.load("../res/intro_ball.gif")
    ball_rect = ball.get_rect()
    paddle = pygame.Rect(30, size[1] / 2 - 25, 10, 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_w]:
                paddle = paddle.move(0, -3)
            if pygame.key.get_pressed()[pygame.K_s]:
                paddle = paddle.move(0, 3)

        # if ball_rect.right > size[0]:
        #     speed[0] = -speed[0]
        # if ball_rect.left < 0:
        #     speed[0] = -speed[0]
        # if ball_rect.top < 0:
        #     speed[1] = -speed[1]
        # if ball_rect.bottom > size[1]:
        #     speed[1] = -speed[1]
        # ball_rect = ball_rect.move(speed)
        screen.fill(color)
        pygame.draw.rect(screen, (0, 0, 0), paddle)
        # screen.blit(ball, ball_rect)
        pygame.display.flip()
        time.sleep(0.05)
