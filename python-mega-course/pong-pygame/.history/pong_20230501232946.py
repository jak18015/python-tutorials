import pygame, sys

# general setup
pygame.init()
clock=pygame.time.Clock()

# setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# game rectangle
ball = pygame.rect((screen_width-15),(screen_height-15),30,30)
player = pygame.Rect(screen_width-20,screen_height-70,10,140)
opponent = pygame.Rect(10,screen_height-70,10,140)

bg_color = pygame.color('black')
light_grey = (200,200,200)

while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # visuals
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,)

    # updating the window
    pygame.display.flip()
    clock.tick(60)



