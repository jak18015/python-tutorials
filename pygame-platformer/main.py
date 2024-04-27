# Import dependencies
from assets import *
import os

# Center game window
os.environ['SDL_VIDEO_WINDOW_CENTERED'] = '1'

# Initialize pygame engine
pygame.init()

# Create display
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # width, height in px
pygame.display.set_caption("The world's greatest game!") # game window caption

# Sprites
player_img = 'assets/images/gothic-hero-idle.gif'
enemy_img = 'assets/images/demon-idle.gif'
number_of_enemies: int = 10
## group sprites
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
for i in range(number_of_enemies):
    enemies.add(Enemy(DISPLAY_SURF, enemy_img, 5))
    all_sprites.add(Enemy(DISPLAY_SURF, enemy_img, 5))
all_sprites.add(Player(DISPLAY_SURF, player_img, 5))

# Game Loop
while True:
    # quitting the game loop by closing the window
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # move sprites and draw the image
    move_sprites(all_sprites)
    DISPLAY_SURF.fill('BLACK')
    draw_sprites(all_sprites)

    # update the display
    pygame.display.update()
    FPS.tick(framerate)