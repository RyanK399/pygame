import pygame
import time

#starter code 
pygame.init() # initialize a pygame class
#set our screen size
width, height = 400, 400
screen  = pygame.display.set_mode((width, height))



backround_colour = 255, 0, 0 #set backround color



#load in our image
duck = pygame.image.load("IMG_4687.jpg")
duck = pygame.transform.scale(duck, (50, 40))
duck_rect = duck.get_rect()


#Sets Image(Duck) speed
duck_speed = [1,1]


#main running loop
running = True
while running:
    #create an event in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #close the game
            running = False



    screen.fill(backround_colour) # makes screen the background colour



    screen.blit(duck, duck_rect) # adds image to the rect
    duck_rect = duck_rect.move(duck_speed)


    print(duck_rect.topleft)


    #bound image(duck) in our screen
    if duck_rect.left < 0 or duck_rect.right > width:
        duck_speed[0] = -duck_speed[0]
    if duck_rect.top < 0 or duck_rect.bottom > height:
       duck_speed[1] = -duck_speed[1]
   


    pygame.display.flip() #refreshes the screen
    time.sleep(10 / 1000) #Slowed down image(duck)


pygame.quit() #quits pygame properly



    
