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
ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)

opponent = pygame.Rect(10,screen_height/2-70,10,140)
player = pygame.Rect(screen_width-20,screen_height/2-70,10,140)
bg_color = pygame.Color('black')
light_grey = (200,200,200)

while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # visuals
    pygame.draw.rect(screen,'orange',player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,'black',(screen_width/2,0), (screen_width/2, screen_height))

    # updating the window
    pygame.display.flip()
    clock.tick(60)



