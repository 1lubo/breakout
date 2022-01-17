# import pygame
from operator import length_hint
import pygame

#define color
BLACK = (0,0,0)

# define class
class Paddle(pygame.sprite.Sprite):
    # this class represents a paddle. It derives from the "Sprite" class in Pygame

    def __init__(self, color, width, height) -> None:
        # call the parent class (Sprite) constructor
        super().__init__()

        # pass in the color of the paddle, its width and height
        # set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw the paddle (a rectangle)
        pygame.draw.rect(self.image, color, [0,0, width, height])

        # fetch the rectangle object that has the dimension of the image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # check that you are not going too far (off the screen)
        if self.rect.x < 0:
            self.rect.x = 0
    
    def moveRight(self, pixels):
        self.rect.x += pixels
        # check that you are not going too far (off the screen)
        if self.rect.x > 700:
            self.rect.x = 700