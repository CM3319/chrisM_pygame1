from turtle import Screen
import pygame
import sys

pygame.init()
w = 800 
h = 600


screem = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()


pygame.display.set_caption('Fario')

class Player:
    def __init__(self):
        size = (40,60)
        position =(100, h-150)
        vel =[0,0]
        speed = 5
        jumpPower =-15
        graviity = 1
        on_ground = False
def input(self, keys):
    if keys[pygame.K_LEFT]:
        self.vel[0] =-self.speed
    elif keys[pygame.K_RIGHT]:
        self.vel[0] = self.pygame.speed
    else:
        self.vel[0] = 0 

    if keys[pygame.K_SPACE] and self.onGround:
        self.vel[1] = self.jump

     
  

         

    

scroll_x  





running = True

while running:
    clock.tick(60)
    screen.fill((255, 255, 255))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()


            pygame.display.flip()