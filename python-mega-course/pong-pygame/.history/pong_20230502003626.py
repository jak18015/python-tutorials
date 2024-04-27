import pygame, sys, random
from pygame import freetype

# general setup
pygame.init()
clock=pygame.time.Clock()

# setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# text
freetype.get_default_font()
GAME_FONT = pygame.freetype.Font("arial.ttf", 24)

# game rectangles
ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player = pygame.Rect(10,screen_height/2-70,10,140)
opponent = pygame.Rect(screen_width-20,screen_height/2-70,10,140)
court = pygame.Rect(screen_width/2-15,screen_height/2-15,60,60)

# base speed
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 0

# ball animation
def ball_animation():
    global ball_speed_x, ball_speed_y
    # ball delta
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # boundary collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_reset()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
def ball_reset():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top =0
    if player.bottom >= screen_height:
        player.bottom = screen_height
def opponent_animation():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top =0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
def player_movement():
    global player_speed
    player_keys = pygame.key.get_pressed()
    if player_keys[pygame.K_w]:
        player_speed = -7
    elif player_keys[pygame.K_s]:
        player_speed = 7
    else:
        player_speed = 0
def opponent_movement():
    global opponent_speed
    opponent_keys = pygame.key.get_pressed()
    if opponent_keys[pygame.K_UP]:
        opponent_speed = -7
    elif opponent_keys[pygame.K_DOWN]:
        opponent_speed = 7
    else:
        opponent_speed = 0

# game loop
while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    player_movement()
    opponent_movement()
    ball_animation()
    player_animation()
    opponent_animation()

    # visuals
    screen.fill('black')
    pygame.draw.circle(screen,(200,200,200),radius=100, center=(screen_width/2,screen_height/2))
    pygame.draw.circle(screen,'black',radius=99, center=(screen_width/2,screen_height/2))
    pygame.draw.aaline(screen,(200,200,200),(screen_width/2,0), (screen_width/2, screen_height))
    pygame.draw.rect(screen,'orange',player)
    pygame.draw.rect(screen,'cyan',opponent)
    pygame.draw.ellipse(screen,'white',ball)
    
    #scorer
    GAME_FONT.render_to(screen, (40, 350), "Hello World!", (0, 0, 0))

    # updating the window
    pygame.display.update()
    clock.tick(60)



