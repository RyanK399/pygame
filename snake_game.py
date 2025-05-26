
import pygame
import time

#define colors
black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0


#starter code 
pygame.init() # initialize a pygame class
#set our screen size
width, height = 720, 480
pygame.display.set_caption ('Snake')
screen  = pygame.display.set_mode((width, height))

#snake information'
snake_position = [360, 240]
snake_speed = 10
snake_direction = 'RIGHT'
snake_body = [[360,240], [350,240], [340,240],[330,240]]


running = True
while running:
   screen.fill(black)
   for event in pygame.event.get():
        if event.type == pygame.QUIT: #close the game
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP: 
                 snake_direction = 'UP'
            if event.key == pygame.K_DOWN:
                 snake_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                 snake_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                 snake_direction = 'RIGHT'
     
     
     
#Set the snake on the screen
for pos in snake_body:
    pygame.draw.rect(screen, green, pygame.Rect(pos[0],pos[1],10,10))

if snake_direction =='UP':
     snake_position[1] -= snake_speed
if snake_direction =='DOWN':
     snake_position[1]+= snake_speed
if snake_direction =='RIGHT':
     snake_position[0] += snake_speed
if snake_direction =='LEFT':
     snake_position[0] -= snake_speed

snake_body.insert(0,list(snake_position))
snake_body.pop


pygame.display.flip() 

clock = pygame.time.Clock()
clock.tick(60)


pygame.quit() #quits pygame properly

