import imp
import pygame
from random import randint
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    # this class represents a ball. It derives from the "Sprite" calss in pygame

    def __init__(self, color, width, height) -> None:
        super().__init__()

        # pass the color of the ball, its width and height
        #set the background color and set ut to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw the ball (a rectagle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4,8), randint(-8,8)]

        # fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)