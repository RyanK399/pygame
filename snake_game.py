import pygame
import time

# colors
black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0

pygame.init()
width, height = 640, 480
pygame.display.set_caption("Smnake")
screen = pygame.display.set_mode((width, height))

# snake info
snake_pos = [320, 240]
snake_spd = 10
snake_dir = 'RIGHT'
snake_body = [[320, 240],
              [304, 240],
              [288, 240],
              [272, 240]
              ]

running = True
while running: 
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != 'DOWN':
                snake_dir = 'UP'
            if event.key == pygame.K_DOWN and snake_dir != 'UP':
                snake_dir = 'DOWN'
            if event.key == pygame.K_LEFT and snake_dir != 'RIGHT':
                snake_dir = 'LEFT'
            if event.key == pygame.K_RIGHT and snake_dir != 'LEFT':
                snake_dir = 'RIGHT'

    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 16, 16))
    
    if snake_dir == 'UP':
        snake_pos[1] -= snake_spd
    if snake_dir == 'DOWN':
        snake_pos[1] += snake_spd
    if snake_dir == 'RIGHT':
        snake_pos[0] += snake_spd
    if snake_dir == 'LEFT':
        snake_pos[0] -= snake_spd

    snake_body.insert(0, list(snake_pos))
    snake_body.pop()

    pygame.display.flip()

    clock = pygame.time.Clock()
    clock.tick(snake_spd)

pygame.quit()