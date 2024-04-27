import pygame, sys

# general setup
pygame.init()
clock=pygame.time.Clock()

# game rectangle
ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player = pygame.Rect(10,screen_height/2-70,10,140)
opponent = pygame.Rect(screen_width-20,screen_height/2-70,10,140)

# setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')



# speed
ball_speed_x = 7
ball_speed_y = 7


while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    



    # visuals
    screen.fill('black')
    pygame.draw.aaline(screen,(200,200,200),(screen_width/2,0), (screen_width/2, screen_height))
    pygame.draw.rect(screen,'orange',player)
    pygame.draw.rect(screen,'cyan',opponent)
    pygame.draw.ellipse(screen,'white',ball)
    

    # updating the window
    pygame.display.flip()
    clock.tick(60)



