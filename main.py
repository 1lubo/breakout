# import the pygame library and initialise the game engine

from ast import While
from tkinter.messagebox import NO
from turtle import Screen
import pygame
from paddle import Paddle

pygame.init()

# define colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

score = 0
lives = 3

# open a new window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

# this will be a list that will contain all the sprites we intend to use
all_sprites_list = pygame.sprite.Group()

# create the paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# add the paddle to the list of sprites
all_sprites_list.add(paddle)

# the look will carry on until the user eists the game (e.g. clicks the close button)
carryOn = True

# the clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop --------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # user did something
        if event.type == pygame.QUIT: # if user clicked close
            carryOn = False # flag what we are done so we exit this loop

    # --- game logic

    
    # --- drawing code goes here
    # first, clear the screen to dark blue
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0,38],[800,38],2)

    # display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: "+ str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: "+ str(lives), 1, WHITE)
    screen.blit(text, (650,10))

    # draw all the sprites
    all_sprites_list.draw(screen)

    # --- update the screen with what we've drawn
    pygame.display.flip()

    # --- limit to 60 frames per second
    clock.tick(60)

# once we have exited the main program loop we can stop the game engine
pygame.quit()
