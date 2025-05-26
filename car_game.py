




import pygame


#Let's import the car class
from car import Car


pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))


GREEN = (100, 255, 200)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


#Create a list that will contain all our sprites
all_sprite_list = pygame.sprite.Group()
playerCar1 = Car(RED, 20, 30)
playerCar1.rect.x = 200
playerCar1.rect.y = 300


playerCar2 = Car(PURPLE, 20, 30)
playerCar2.rect.x = 100
playerCar2.rect.y = 100


#Add our sprites to the list
all_sprite_list.add(playerCar1)
all_sprite_list.add(playerCar2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    #Draw all our sprites
    all_sprite_list.update()
    all_sprite_list.draw(screen)


    pygame.display.flip()




pygame.quit()



