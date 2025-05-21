



import pygame
import time
import random

#starter code 
pygame.init() # initialize a pygame class
#set our screen size
width, height = 400, 400
screen  = pygame.display.set_mode((width, height))


backround_colour = 255, 0, 0 #set backround color



#load in our image
duck = pygame.image.load("IMG_4687.jpg")
duck = pygame.transform.scale(duck, (50, 50))
duck_rect = duck.get_rect()


#load in our image
crosshairs = pygame.image.load("crosshair.png")
crosshairs = pygame.transform.scale(crosshairs, (20, 20))
crosshairs_rect = crosshairs.get_rect()
pos = [200,200]

#Sets Image(Duck) speed
duck_speed = [1,1]


#main running loop
running = True
while running:
    #create an event in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #close the game
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
    
            pos = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos = (crosshairs_rect.center[0]-5 , crosshairs_rect.center[1])
            if event.key == pygame.K_RIGHT:
                pos = (crosshairs_rect.center[0]+5 , crosshairs_rect.center[1])
            if event.key == pygame.K_UP:
                pos = (crosshairs_rect.center[0] , crosshairs_rect.center[1]-5)
            if event.key == pygame.K_DOWN:
                pos = (crosshairs_rect.center[0] , crosshairs_rect.center[1]+5)


#set the center of the crosshair as pos
    crosshairs_rect.center = pos

    screen.fill(backround_colour) # makes screen the background colour



    screen.blit(duck, duck_rect) # adds image to the rect
    crosshairs_rect.center = pos
    screen.blit(crosshairs,crosshairs_rect)
    """
    duck_rect = duck_rect.move(duck_speed)


    #print(duck_rect.topleft)


    #bound image(duck) in our screen
    if duck_rect.left < 0 or duck_rect.right > width:
        duck_speed[0] = -duck_speed[0]
    if duck_rect.top < 0 or duck_rect.bottom > height:
       duck_speed[1] = -duck_speed[1]
   """

    pygame.display.flip() #refreshes the screen

    time.sleep(10 / 1000) #Slowed down image(duck)

pygame.quit() #quits pygame properly