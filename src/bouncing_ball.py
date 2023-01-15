import sys
import time

import pygame


def bounce():
    pygame.init()
    size = (700, 400)
    #color = pygame.Color.cmy
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (110, 110, 110)
    speed = [1, 2]
    screen = pygame.display.set_mode(size)
    margin_to_border = 30
    paddle_size = (50, 100)
    screen_saver = pygame.display.get_allow_screensaver()

    counter = time.time()
    screen_saver_time = 3



    ball = pygame.image.load("../res/intro_ball.gif")
    ball_rect = ball.get_rect()
    paddle_left = pygame.Rect(margin_to_border, size[1] / 2 - paddle_size[1] / 2, paddle_size[0], paddle_size[1])
    paddle_right = pygame.Rect(size[0] - margin_to_border - paddle_size[0], size[1]/ 2 - paddle_size[1] / 2, paddle_size[0], paddle_size[1])
    while True:
        for event in pygame.event.get():
            counter = time.time()
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()

            if pygame.key.get_pressed()[pygame.K_w] and paddle_left.top > 0:
                paddle_left = paddle_left.move(0, -8)
            if pygame.key.get_pressed()[pygame.K_s] and paddle_left.bottom < size[1]:
                paddle_left = paddle_left.move(0, 8)
        if time.time() - counter > screen_saver_time:
            screen.fill(BLACK)
            if ball_rect.right > size[0]:
                speed[0] = -speed[0]
            if ball_rect.left < 0:
                speed[0] = -speed[0]
            if ball_rect.top < 0:
                speed[1] = -speed[1]
            if ball_rect.bottom > size[1]:
                speed[1] = -speed[1]
            ball_rect = ball_rect.move(speed)
            screen.blit(ball, ball_rect)
        else:
            screen.fill(GRAY)
            pygame.draw.rect(screen, (0, 0, 0), paddle_left)
            pygame.draw.rect(screen, (255, 255, 255), paddle_right)
        pygame.display.flip()
        time.sleep(0.05)
