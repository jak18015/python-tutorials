import pygame
from ..packages.gif_pygame import gif_pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, display_surf, img, movement_speed) -> None:  # The constructor method
        super().__init__()  # Calling the parent class constructor
        self.display_surf = display_surf # get the display surface
        self.screen_width = display_surf.get_width() # display width
        self.screen_height = display_surf.get_height() # display height
        
        self.image = gif_pygame.load(img) # Load the image to use for the character
        self.rect = self.image.get_rect() # Get the rectangle bounding the character image
        self.rect.center = (0.5*self.screen_width-0.5*self.rect.width, 0.9*self.screen_height-0.5*self.rect.height) # Place the character

        self.movement_speed = movement_speed

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        self.move_L = -self.movement_speed if pressed_keys[pygame.K_a] else 0
        self.move_R =  self.movement_speed if pressed_keys[pygame.K_d] else 0
        self.move_U = -self.movement_speed if pressed_keys[pygame.K_w] else 0
        self.move_D =  self.movement_speed if pressed_keys[pygame.K_s] else 0

        self.x = self.move_L + self.move_R
        self.y = self.move_U + self.move_D

        vector = pygame.math.Vector2(self.x, self.y)
        vector.scale_to_length(self.movement_speed*1.2) if vector.magnitude() > self.movement_speed else vector

        self.rect.move_ip(vector)

    def draw(self): # draw sprite to display, passing the image and rectangle as arguments
        if self.x < 0:
            self.display_surf.blit(pygame.transform.flip(self.image.blit_ready(), True, False), self.rect)
        else:
            self.display_surf.blit(self.image.blit_ready(), self.rect)