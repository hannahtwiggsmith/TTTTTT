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
		self.x = 2
		self.prev = 0
		pygame.key.set_repeat(1)
	def MainLoop(self):
		while 1:
			clock.tick(60)
			self.turtle.gravity(self.x)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == KEYDOWN:
					if ((event.key == K_RIGHT)
					or (event.key == K_LEFT)):
					#or (event.key == K_SPACE)):
						self.turtle.move(event.key)
						self.prev = 0
					elif (event.key == K_SPACE):
						if self.prev == 0:
							self.x = -self.x
							self.prev = 1
			self.screen.fill(self.black)
			self.turtle_sprites.draw(self.screen)
			pygame.display.flip()
	def LoadSprites(self):
		self.turtle = Turtle()
		self.turtle_sprites = pygame.sprite.RenderPlain((self.turtle))



class Turtle(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('turtle.png', -1)
		#self.image2, self.rect = load_image('turtleright.png', -1)
	def gravity(self, x):
		self.rect.move_ip(0,x)
	def move(self, key):
		xMove = 0
		yMove = 0
		if (key == K_RIGHT):
			xMove = 10
			#self.image, self.rect = load_image('turtleright.png', -1)
		elif (key == K_LEFT):
			xMove = -10
		# elif (key == K_SPACE):
		# 	self.x = -self.x
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