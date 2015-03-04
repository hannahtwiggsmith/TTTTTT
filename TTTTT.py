import os, sys
import pygame
from pygame.locals import *

clock = pygame.time.Clock()

def load_image(name, colorkey = None):
	fullname = os.path.join('media/images', name)
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
		self.LoadSprites()
	def MainLoop(self):
		while 1:
			clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == KEYDOWN:
					if ((event.key == K_RIGHT)
					or (event.key == K_LEFT)):
						self.turtle.move(event.key)
			self.screen.fill(self.black)
			self.turtle_sprites.draw(self.screen)
			pygame.display.flip()
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
		    Turtle.pos.left -=10
	def LoadSprites(self):
		self.turtle = Turtle()
		self.turtle_sprites = pygame.sprite.RenderPlain((self.turtle))



class Turtle(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('turtle.png', -1)
	def move(self, key):
		xMove = 0
		yMove = 0
		if (key == K_RIGHT):
			xMove = 10
		self.rect.move_ip(xMove,yMove)
# class level(levelBase.Level):
# 	def __init__(self):
# 		self.BLOCK = 1
# 		self.TURTLE = 2
# 	def getLayout(self):
# 		return [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
# 		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
# 		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
# 		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
# 		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
# 		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\

if __name__ == "__main__":
	MainWindow = TTTTTMain()
	MainWindow.MainLoop()