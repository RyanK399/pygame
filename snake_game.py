

import pygame


#Define colours
black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0


#Initial screen stuff
pygame.init()
width, height = 720, 480
pygame.display.set_caption('ICS3U/C1 Snake Game')
screen = pygame.display.set_mode((width, height))


#Snake Information
snake_position = [360, 240]
snake_speed = 10
direction = 'RIGHT'
snake_body = [[360,240],[350,240],[340,240],[330,240]]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'


    screen.fill(black) #Fill in the screen


    #Set the snake on the screen
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
   
    #Moving the snake
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10


    snake_body.insert(0, list(snake_position))
    snake_body.pop()


    pygame.display.flip()


    #Create a clock
    clock = pygame.time.Clock()
    clock.tick(snake_speed)


pygame.quit()


