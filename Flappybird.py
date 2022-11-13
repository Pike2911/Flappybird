from asyncio.windows_utils import pipe
import pip
import pygame
import sys
import random
import os
#-----------------------------------------------------------------
# init
#-----------------------------------------------------------------

pygame.init()
gravity = 0.1
screen = pygame.display.set_mode((1980,1080 ), pygame.FULLSCREEN)
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background-day-1980x1080.png')
base_surface = pygame.image.load("assets/base-1980x1080.png")
base2_surface = pygame.image.load('assets/base-1980x1080.png')
bird_surface = pygame.image.load('assets/redbird-downflap(big).png')
greenpipe_surface = pygame.image.load('assets/pipe-green.png')
greenpipe_re = pygame.image.load('assets/pipe-green_re.png')


bird_surface = pygame.transform.scale(bird_surface, (100,60))
bird_rect = bird_surface.get_rect( center=(550,450) )
bird_velocity = 0.0
x = 0

start_point = 1980
start_point_re = 1980
greenpipe_surface = pygame.transform.scale(greenpipe_surface, (70,500))
greenpipe_re = pygame.transform.scale(greenpipe_re, (70,500))
pipe_rects = []
pipe_rect_res = []
for i in range(500):
    hight = 400 + random.randint(5, 150)
    pipe_rects.append(greenpipe_surface.get_rect(midtop=(start_point,hight)))
    start_point += 300

for i in range(500):
    hight = 100 + random.randint(5, 150)
    pipe_rect_res.append(greenpipe_re.get_rect(midbottom=(start_point_re,hight)))
    start_point_re += 300
#-----------------------------------------------------------
# game loop
#-----------------------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                bird_velocity = 0.0
                bird_velocity += 5

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = 0.0
                bird_velocity -= 5

    for pipe_rect in pipe_rects:
        if bird_rect.colliderect(pipe_rect):
            sys.exit()
    for pipe_rect_re in pipe_rect_res:
        if bird_rect.colliderect(pipe_rect_re):
            sys.exit()
        





    x = x - 1



    screen.blit(bg_surface, (0, 0))

    for pipe_rect in pipe_rects:
        pipe_rect.x -=1
        screen.blit(greenpipe_surface, pipe_rect)
    
    for pipe_rect_re in pipe_rect_res:
        pipe_rect_re.x -=1
        screen.blit(greenpipe_re, pipe_rect_re)

    # for pipe_rect_re in pipe_rect_res:
    #     pipe_rect_re.x -=1
    #     screen.blit(greenpipe_re, pipe_rect_re)




    screen.blit(base_surface, (x,780))
    screen.blit(base2_surface, (x +1980,780 ))


    bird_velocity += gravity
    bird_rect.y += bird_velocity
    screen.blit(bird_surface, bird_rect)



    pygame.display.update()
    clock.tick(144)

    if x <= -1980:
        x = 0
