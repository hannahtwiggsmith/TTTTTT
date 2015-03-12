import os, sys
import pygame
import random
from pygame.locals import *

clock = pygame.time.Clock()

def load_image(name, colorkey = None):
    fullname = os.path.join('data/images', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey != None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Turtle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('turtle.png', -1)
        self.rect.x = 50
        self.rect.y = 550
        self.black = 0,0,0
        self.x = 5
        self.prev = 0
        pygame.key.set_repeat(1)

    def gravity(self, x):
        self.rect.move_ip(0,x)

    def move(self, key):
        self.xMove = 0
        self.yMove = 0
        if (key == K_RIGHT):
            self.xMove = 20
            self.image = pygame.image.load('data/images/turtle_right.png')
        elif (key == K_LEFT):
            self.xMove = -20
            self.image = pygame.image.load('data/images/turtle.png')

        for wall in left_wall:
            if self.rect.colliderect(wall.rect):
                self.rect.left = wall.rect.right
        self.rect.move_ip(self.xMove,self.yMove)

    def update(self):
        #self.image.fill((0,0,0))
        self.gravity(self.x)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if ((event.key == K_RIGHT)
                or (event.key == K_LEFT)):
                    self.move(event.key)
                    self.prev = 0
                elif (event.key == K_SPACE):
                    if self.prev == 0:
                        self.x = -self.x
                        self.prev = 1

        for wall in top_wall:
            if self.rect.colliderect(wall.rect):
                self.rect.top = wall.rect.bottom
        for wall in lower_wall:
            if self.rect.colliderect(wall.rect):
                self.rect.bottom = wall.rect.top
        for scary in scaries:
            if self.rect.colliderect(scary.rect):
                sys.exit()


class Evil_Block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('evil_block.png', -1)

        self.rect.y = y
        self.rect.x = x

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.image.load('data/images/block.png')
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

all_sprite_list = pygame.sprite.Group()
top_wall = pygame.sprite.Group()
left_wall = pygame.sprite.Group()
right_wall = pygame.sprite.Group()
lower_wall = pygame.sprite.Group()
scaries = pygame.sprite.Group()

for i in range(0,16):
    wall = Wall(i*50, 0)
    top_wall.add(wall)
    all_sprite_list.add(wall)
 
for i in range(0,12):
    wall = Wall(0, i*50)
    left_wall.add(wall)
    all_sprite_list.add(wall)

for i in range(0,12):
    wall = Wall(750, i*50)
    right_wall.add(wall)
    all_sprite_list.add(wall)

for i in range(0,16):
    wall = Wall(i*50, 550)
    lower_wall.add(wall)
    all_sprite_list.add(wall)

for i in range (0,20):
    x = random.randrange(50,750,100)
    y = random.randrange(1,650,100)
    scary = Evil_Block(x,y)
    scaries.add(scary)

class TTTTTMain:

    def __init__(self):
        pygame.init()
        self.black = 0, 0, 0

        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):

        self.LoadTurtle()

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))

        pygame.display.flip()
        all_sprite_list.draw(screen)
        scaries.draw(screen)
        while 1:
            clock.tick(60)

            self.turtle_sprites.clear(self.screen, self.background)

            self.turtle.update()

            self.turtle_sprites.draw(self.screen)

            pygame.display.flip()

    def LoadTurtle(self):
        self.turtle = Turtle()
        self.turtle_sprites = pygame.sprite.RenderPlain((self.turtle))
        #self.mask = pygame.mask.from_surface(self.turtle.image)
    def loser(self):
        self.screen.fill(self.black)
        load_image('lose.png')
        pygame.display.flip()

if __name__ == "__main__":
    MainWindow = TTTTTMain()
    MainWindow.MainLoop()