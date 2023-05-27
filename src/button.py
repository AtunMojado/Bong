import pygame
from typing import Tuple
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 42)
margin_left_text = 10
margin_top_text = 25
class Button():
    def __init__(self, screen: pygame.Surface, color: Tuple[int, int, int], left: int, top: int, width: int, height: int):
        self._rect = pygame.Rect(left, top, width, height)
        self._screen = screen
        self._color = color

    def draw(self):
        #text = font.render(text, True, (255, 255, 255))
        pygame.draw.rect(self._screen, self._color, self._rect)

        #self._screen.blit(text, rect)
    def click(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self._rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                action = True
        return action
    def text(self, text: str):
        self._screen.blit(font.render(text, True, (255, 255, 255)), (self._rect[0] + margin_left_text, self._rect[1] + margin_top_text))
        #text1 = font.render(text, True, (255, 255, 255))
        #rect = text1.get_rect(midleft=(self._screen.get_size()[0]//2, self._screen.get_size()[1]//2))
        #self._screen.blit(text1, rect)
