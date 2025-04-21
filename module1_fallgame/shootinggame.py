import pygame 
import random


pygame.init()

screen = pygame.display.set_mode(800,600)
pygame.display.set_caption('Shooter Game')

class Player():
    def __init__(self):
        super(). __init__()
        self.image = pygame.Surface((50,30))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.center = (400,550)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -=5
        if keys[pygame.K_RIGHT]:
            self.rect.x +=5


class Bullet():
    def __init__(self,x,y): 
        super(). __init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center =(x,y)

    def update(self):
        self.rect.y -=7 
        if self.rect.bottom< 0:
            self.kill()

class Enemy():
    def __init__ (self):
        super(). __init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0)) 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 750)
        self.rect.y = random.randint(-200, -50)






    def update(self):
        self.rect.y +=3
        if self.rect.top > 600:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, 750)

# all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


bullets = pygame.sprite.Group()


enemies = pygame.sprite.Group()


for __ in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)


bullets = pygame.sprite.Group

enemies = pygame.sprite.Group



for __ in range(5):
    enemy= Enemy


     




running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
