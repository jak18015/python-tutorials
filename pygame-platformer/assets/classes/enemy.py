import pygame
import random
from ..packages.gif_pygame import gif_pygame

# This class represents an enemy character in the game
class Enemy(pygame.sprite.Sprite):  # Inheriting from the pygame sprite class
    def __init__(self, display_surf, img, movement_speed) -> None:  # The constructor method
        super().__init__()  # Calling the parent class constructor

        # get the display surface and dimensions
        self.display_surf = display_surf
        self.screen_width = display_surf.get_width()
        self.screen_height = display_surf.get_height()
        
        self.movement_speed = movement_speed

        # create the image and bounding rectangle of the character
        self.image = gif_pygame.load(img) # Load the image to use for the enemy character
        self.rect = self.image.get_rect() # Get the rectangle bounding the character image
        self.rect.centerx = (random.randint(self.rect.width, self.screen_width-2*self.rect.width))
        self.rect.top = 0
    
    # Method to move the enemy character
    def move(self):
        self.y = self.movement_speed
        if self.rect.top == 0 or self.rect.bottom > self.screen_height:
            self.rect.centerx = (random.randint(0, self.screen_width))
            self.rect.top = 0
            self.x = random.randint(-self.movement_speed, self.movement_speed)
        self.rect.move_ip(self.x, self.y)

    # draw sprite to display, passing the image and rectangle as arguments
    def draw(self): # draw sprite to display, passing the image and rectangle as arguments
        if self.x > 0:
            self.display_surf.blit(pygame.transform.flip(self.image.blit_ready(), True, False), self.rect)
        else:
            self.display_surf.blit(self.image.blit_ready(), self.rect)
