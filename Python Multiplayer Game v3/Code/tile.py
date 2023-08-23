import pygame 
from settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups,image,id):
		super().__init__(groups)
		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.id = id