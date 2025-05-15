

import pygame

pygame.init() # initialize a pygame class

#set our screen size
width, height = 400, 400
screen  = pygame.display.set_mode((width, height))

backround_colour = 255, 0, 0 #set backround color

#load in our image
duck = pygame.image.load("IMG_4687.jpg")
duck = pygame.transform.scale(duck, (50, 40))
duck_rect = duck.get_rect()

#main running loop
running = True
while running:
    #create an event in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #close the game
            running = False

    screen.fill(backround_colour) # makes screen the backround colour

    screen.blit(duck, duck_rect)



    pygame.display.flip() #refreshes the screen

pygame.quit() #quits pygame properly
    
