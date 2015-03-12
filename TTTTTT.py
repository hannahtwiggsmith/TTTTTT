import os, sys
import pygame
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
        self.black = 0,0,0
        self.x = 5
        self.prev = 0
        pygame.key.set_repeat(1)

    def gravity(self, x):
        self.rect.move_ip(0,x)

    def move(self, key):
        xMove = 0
        yMove = 0
        if (key == K_RIGHT):
            xMove = 20
            self.image = pygame.image.load('data/images/turtle_right.png')
        elif (key == K_LEFT):
            xMove = -20
            self.image = pygame.image.load('data/images/turtle.png')
        self.rect.move_ip(xMove,yMove)

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


class Evil_Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('evil_block.png', -1)

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
wall_list = pygame.sprite.Group()

for i in range(0,16):
    wall = Wall(i*50 - 450, -275)
    wall_list.add(wall)
    all_sprite_list.add(wall)
 
for i in range(0,12):
    wall = Wall(-450, i*50 - 275)
    wall_list.add(wall)
    all_sprite_list.add(wall)

for i in range(0,12):
    wall = Wall(300, i*50 - 275)
    wall_list.add(wall)
    all_sprite_list.add(wall)

for i in range(0,16):
    wall = Wall(i*50 - 450, 275)
    wall_list.add(wall)
    all_sprite_list.add(wall)

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
        while 1:
            clock.tick(60)

            self.turtle.update()

            self.turtle_sprites.draw(self.screen)

            pygame.display.flip()

    def LoadTurtle(self):
        self.turtle = Turtle()
        self.turtle_sprites = pygame.sprite.RenderPlain((self.turtle))
        self.mask = pygame.mask.from_surface(self.turtle.image)


if __name__ == "__main__":
    MainWindow = TTTTTMain()
    MainWindow.MainLoop()