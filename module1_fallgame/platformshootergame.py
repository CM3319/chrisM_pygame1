import pygame
import os
import randomb
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

#set framerate
clock = pygame.time.Clock()
FPS = 60


#define game variables
GRAVITY = 0.75
TILE_SIZE = 40

#define player action variables
moving_left = False
moving_right = False
shoot = False
grenade = False
grenade_thrown = False
