import pygame  # Importing the Pygame library for graphics and audio
from pygame.locals import *  # Importing all constants from the Pygame library
import sys  # Importing the sys module for exiting the program
from assets.classes.player import Player
from assets.classes.enemy import Enemy

'''
gif_pygame credit to Zeperox
https://github.com/Zeperox/gif-pygame.git
'''
from assets.packages.gif_pygame.gif_pygame import load, PygameGIF, GIFPygame, version
import assets.packages.gif_pygame.transform as transform

'''
Sprites from Ansimuz
https://ansimuz.itch.io/gothicvania-patreon-collection
'''

# Assigning colors (RGB)
BLACK = pygame.Color(  0,   0,   0)
WHITE = pygame.Color(255, 255, 255)
GREY  = pygame.Color(128, 128, 128)
BLUE  = pygame.Color(  0,   0, 255)
GREEN = pygame.Color(  0, 255,   0)
RED   = pygame.Color(255,   0,   0)

# Set frames per second
framerate = 60
FPS = pygame.time.Clock() # instantiates an object called FPS with the class pygame.time.Clock()

def move_sprites(sprite_group):
    for entity in sprite_group:
        # player.move() if entity == player else enemy.move()
        entity.move()
def draw_sprites(sprite_group):
    for entity in sprite_group:
        entity.draw()