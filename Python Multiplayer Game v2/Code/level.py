import pygame 
from settings import *
from tile import Tile


class Level(Config):
	def __init__(self):
		Config.__init__(self)

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = pygame.sprite.Group()
		self.obstacle_sprites = pygame.sprite.Group()
    
		# sprite setup
		self.create_map()

	def create_map(self):
		for row_index,row in enumerate(self.WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * self.TILESIZE
				y = row_index * self.TILESIZE
				#print(x,y)
				if col == 'x':
					Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'Graphics/rock.png')
				#if col == ' ':
			#		Player((x,y),[self.visible_sprites])

	def run(self):
		# update and draw the game
		# creating the floor
		self.visible_sprites.draw(self.display_surface)
		self.visible_sprites.update()