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

class TTTTTMain:

    def __init__(self, width = 640, height = 480):
        pygame.init()
        self.black = 0, 0, 0

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.x = 5
        self.prev = 0
        pygame.key.set_repeat(1)

    def MainLoop(self):

        self.LoadTurtle()
        self.LoadBlock()

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))

        pygame.display.flip()

        while 1:
            clock.tick(60)
            pos = pygame.sprite.collide_mask(self.turtle,self.block)
            # print pos
            self.turtle.gravity(self.x)  
            if self.x == -5:
                if pos!= None and pos > (450,300):
                    self.n = 5
                    self.turtle.gravity(self.n)
            if self.x == 5:
                if pos != None and pos <= (550,300):
                    self.n = -5
                    self.turtle.gravity(self.n)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)):
                        self.turtle.move(event.key)
                        self.prev = 0
                    elif (event.key == K_SPACE):
                        if self.prev == 0:
                            self.x = -self.x
                            self.prev = 1
            self.screen.fill(self.black)
            self.turtle_sprites.draw(self.screen)
            # for i in range(0,32):
            #     self.block.place(i*24,24)
            #     self.block_sprites.draw(self.screen)
            self.block_sprites.draw(self.screen)
            pygame.display.flip()

    def LoadTurtle(self):
        self.turtle = Turtle()
        self.turtle_sprites = pygame.sprite.RenderPlain((self.turtle))
        self.mask = pygame.mask.from_surface(self.turtle.image)

    def LoadBlock(self):
        self.block = Block()
        self.mask = pygame.mask.from_surface(self.block.image)
        self.block_sprites = pygame.sprite.RenderPlain((self.block))


class Turtle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('turtle.png', -1)

    def gravity(self, x):
        self.rect.move_ip(0,x)

    def move(self, key):
        xMove = 0
        yMove = 0
        if (key == K_RIGHT):
            xMove = 10
            self.image = pygame.image.load('data/images/turtle_right.png')
        elif (key == K_LEFT):
            xMove = -10
            self.image = pygame.image.load('data/images/turtle.png')
        self.rect.move_ip(xMove,yMove)

class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('block.png', -1)
        #self.image = pygame.image.load("data/images/block.png")
        self.rect = pygame.Rect(100,200,24,24)

    # def place(self, left, top, width = 24, height = 24):
    #     self.rect = pygame.rect(left,top,width,height)



if __name__ == "__main__":
    MainWindow = TTTTTMain()
    MainWindow.MainLoop()