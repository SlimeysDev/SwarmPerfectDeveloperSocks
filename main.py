import pygame
import sys
import time
from pygame.locals import *

import cursor
import socks
import input_box

pygame.init()

# FPS settings

FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined colors

BLACK = (0, 0, 0)   
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Display settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY.fill(WHITE)
pygame.display.set_caption("Swarm's perfect developer socks")

# Mouse settings

pygame.mouse.set_visible(False)

# Objects

Cursor = cursor.Cursor()
Socks = socks.Socks()
FemboyInput = input_box.input_box(300, 32, "Enter current femboy level.")

# Variables

femboy_level = 0


# Game loop

while True:

    # Quits the game and close the script upon clicking on the quit button
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            Cursor.clickSound()
            if FemboyInput.rect.colliderect(Cursor.rect):
                FemboyInput.active = not FemboyInput.active
            else:
                FemboyInput.active = False
            FemboyInput.color = FemboyInput.color_active if FemboyInput.active else FemboyInput.color_inactive
        
        if event.type == pygame.KEYDOWN:
            if FemboyInput.active:
                if event.key == pygame.K_RETURN:
                    femboy_level = int(FemboyInput.text)
                    print(femboy_level)
                    FemboyInput.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    FemboyInput.text = FemboyInput.text[:-1]
                else:
                    FemboyInput.text += event.unicode

    
    Cursor.update()

    DISPLAY.fill(WHITE)

    Socks.draw(DISPLAY)
    Cursor.draw(DISPLAY)

    txt_surface = FemboyInput.font.render(FemboyInput.text, True, FemboyInput.color)
    DISPLAY.blit(txt_surface, (FemboyInput.rect.x+5, FemboyInput.rect.y+5))
    pygame.draw.rect(DISPLAY, WHITE, pygame.Rect((100, 184), (300, 32)), 0)
    pygame.draw.rect(DISPLAY, FemboyInput.color, FemboyInput.rect, 2)
    

    pygame.display.update()
    FramePerSec.tick(FPS)
