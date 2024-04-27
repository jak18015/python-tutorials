import pygame, sys
from settings import * # everything from the settings.py file
from level import Level

VERSION = '0.0.1'

class Game:
    def __init__(self):
          
        # general setup
        pygame.init() # initiate pygame
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH)) # create surface
        pygame.display.set_caption(f'Zylda (v{VERSION})')
        self.clock = pygame.time.Clock() # initiate the clock
    
        self.level = Level()

    def run(self): # main loop

        while True: # event loop to close the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black') # first fill the screen with black before updating the display
            self.level.run()
            pygame.display.update() # update the display
            self.clock.tick(FPS) # tick on the clock
 
if __name__ == '__main__':
    game = Game()
    game.run()