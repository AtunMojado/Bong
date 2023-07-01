import sys
import time
import pygame
from src.button import Button
from src.match import Match
from src.screen_fade import ScreenFade

def bounce():
    pygame.init()
    size = (700, 400)
    screen = pygame.display.set_mode(size)
    MENU_BG_COLOR = (10, 170, 0)

    BUTTON_COLOR = (0, 0, 100)
    STARTBUTTON_TOP_MARGIN = 150
    EXITBUTTON_BOTTOM_MARGIN = 50

    INTRO_FADE_COLOR = (10, 170, 0)
    INTRO_FADE_LEFT_POS = 0
    INTRO_FADE_TOP_POS = 0
    INTRO_FADE_WIDTH = screen.get_size()[0]
    INTRO_FADE_HEIGHT = screen.get_size()[1]
    INTRO_FADE_SPEED = 30

    #font = pygame.font.Font('assets/fonts/AtariClassic.ttf', 20)

    button_width, button_height = (300, 90)

    intro_fade = ScreenFade(screen=screen, left=INTRO_FADE_LEFT_POS, top=INTRO_FADE_TOP_POS, width=INTRO_FADE_WIDTH, height=INTRO_FADE_HEIGHT, color=INTRO_FADE_COLOR, speed=INTRO_FADE_SPEED)

    start_button = Button(screen=screen, color=BUTTON_COLOR, left=screen.get_size()[0]//2 - button_width//2, top= screen.get_size()[1]//2 - STARTBUTTON_TOP_MARGIN,
                          width=button_width, height=button_height)
    exit_button = Button(screen=screen, color=BUTTON_COLOR, left=screen.get_size()[0]//2 - button_width//2, top= screen.get_size()[1]//2 + EXITBUTTON_BOTTOM_MARGIN,
                          width=button_width, height=button_height)
    match = Match(screen=screen)

    #game variables
    run = True
    start_game = False







    while run:

        start_click = start_button.click() #pygame.mouse.get_pressed(3)[0]
        exit_click = exit_button.click()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or exit_click:
                sys.exit()

        if start_game == False:
            screen.fill(MENU_BG_COLOR)
            start_button.draw()
            exit_button.draw()
            start_button.text('START BONG')
            exit_button.text(' QUIT  BONG')

            if start_click:
                start_game = True
            pygame.display.flip()

        if start_game == True:
            match.update(events)
            match.display()
            intro_fade.draw()
            intro_fade.move()
            pygame.display.flip()
            time.sleep(0.05)










