from typing import Tuple, List
import pygame

from src.paddle import Paddle
from src.scoreboard import ScoreBoard



class Ball:

    def __init__(self, position: Tuple[int, int], radius: int, speed: Tuple[int, int], color: Tuple[int, int, int],
                 screen: pygame.Surface):
        """Circle that goes all over the screen and collides with the paddles or score goals"""
        self._position = position
        self._radius = radius
        self._speed = speed
        self._color = color
        self._screen = screen
        self._goal_left = False
        self._goal_right = False
        self._rect = pygame.Rect(self._position[0] - self._radius, self._position[1] - self._radius, 20, 20)

    def set_ball_position(self):
        self._position = (350, 200)
    def draw(self):
        ball = pygame.draw.circle(self._screen, self._color, self._position, self._radius)
        return ball
    def move(self, left_paddle: Paddle, right_paddle: Paddle):
        """
        Function to move the ball taking into consideration the collisions with the given paddles.
        :param left_paddle: Paddle on the lef side of the screen
        :param right_paddle: Paddle on the right side of the screen
        :return:
        """
        self._position = (self._position[0] + self._speed[0], self._position[1] + self._speed[1])
        self.wall_collision()
        self.paddle_collision(left_paddle, right_paddle)
    def paddle_collision(self, left_paddle: Paddle, right_paddle: Paddle):
        collision_tolerance = 10
        speed_x = self._speed[0]
        speed_y = self._speed[1]

        #collisions for left paddle
        if abs(self._position[0] - self._radius - left_paddle.rect.right) < collision_tolerance and speed_x < 0 and left_paddle.rect.top < self._position[1] < left_paddle.rect.bottom:
            speed_x *= -1
            self._speed = (speed_x, speed_y)
        if abs(self._position[1] + self._radius - left_paddle.rect.top) < collision_tolerance and speed_y > 0 and left_paddle.rect.left < self._position[0] < left_paddle.rect.right:
            speed_y *= -1
            self._speed = (speed_x, speed_y)
        if abs(self._position[1] - self._radius - left_paddle.rect.bottom) < collision_tolerance and speed_y < 0 and left_paddle.rect.left < self._position[0] < left_paddle.rect.right:
            speed_y *= -1
            self._speed = (speed_x, speed_y)
        if abs(self._position[0] + self._radius - left_paddle.rect.left) < collision_tolerance and speed_x > 0 and left_paddle.rect.top < self._position[1] < left_paddle.rect.bottom:
            speed_x *= -1
            self._speed = (speed_x, speed_y)

        #collisions for right paddle
        if abs(self._position[0] - self._radius - right_paddle.rect.right) < collision_tolerance and speed_x < 0 and right_paddle.rect.top < self._position[1] < right_paddle.rect.bottom:
            speed_x *= -1
            self._speed = (speed_x, speed_y)
        if abs(self._position[1] + self._radius - right_paddle.rect.top) < collision_tolerance and speed_y > 0 and right_paddle.rect.left < self._position[0] < right_paddle.rect.right:
            speed_y *= -1
            self._speed = (speed_x, speed_y)
        if abs(self._position[1] - self._radius - right_paddle.rect.bottom) < collision_tolerance and speed_y < 0 and right_paddle.rect.left < self._position[0] < right_paddle.rect.right:
            speed_y *= -1
            self._speed = (speed_x, speed_y)
        if abs(self._position[0] + self._radius - right_paddle.rect.left) < collision_tolerance and speed_x > 0 and right_paddle.rect.top < self._position[1] < right_paddle.rect.bottom:
            speed_x *= -1
            self._speed = (speed_x, speed_y)





    def wall_collision(self):
        #bottom wall
        if self._position[1] + self._radius > self._screen.get_size()[1]:
            self._speed = (self._speed[0], -abs(self._speed[1]))

        #top wall
        if self._position[1] - self._radius < 0:
            self._speed = (self._speed[0], abs(self._speed[1]))

        if self._position[0] + self._radius < 0:
            self._speed = (abs(self._speed[0]), self._speed[1])
            self._goal_left = True

        #right goal
        if self._position[0] - self._radius > self._screen.get_size()[0]:
            self._speed = (-abs(self._speed[0]), self._speed[1])
            self._goal_right = True
    @property
    def goal_left(self) -> bool:
        """
        Getter to obtain the goal left attribute.
        :return:
        """
        return self._goal_left

    @goal_left.setter
    def goal_left(self, goal_left: bool):
        """
        Setter to set the goal left attribute.
        :param goal_left: The new value for goal left
        :return:
        """
        self._goal_left = goal_left

    @property
    def goal_right(self) -> bool:
        """
        Getter to obtain the goal right attribute.
        :return:
        """
        return self._goal_right

    @goal_right.setter
    def goal_right(self, goal_right: bool):
        """
        Setter to set the goal left attribute.
        :param goal_right: The new value for goal left
        :return:
        """
        self._goal_right = goal_right




    def change_color(self, color):
        self._color = color





























