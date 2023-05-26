import sys
import time
import pygame
from src.button import Button
from src.match import Match

def bounce():
    pygame.init()
    size = (700, 400)
    MENU_BG_COLOR = (10, 170, 0)
    BUTTON_COLOR = (0, 0, 100)
    screen = pygame.display.set_mode(size)
    button_width, button_height = (300, 90)

    start_button = Button(screen=screen, color=BUTTON_COLOR, left=screen.get_size()[0]//2 - button_width//2, top= screen.get_size()[1]//2 - button_height//2,
                          width=button_width, height=button_height)
    match = Match(screen=screen)

    #game variables
    run = True
    start_game = False






    while run:

        left_click = start_button.click() #pygame.mouse.get_pressed(3)[0]
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()

        if start_game == False:
            screen.fill(MENU_BG_COLOR)
            start_button.draw()
            if left_click:
                start_game = True
            pygame.display.flip()



        if start_game == True:
            match.update(events)
            match.display()
            pygame.display.flip()
            time.sleep(0.05)










