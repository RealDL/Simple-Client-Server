import pygame 
from settings import *
from tile import Tile


class Level(Config):
	def __init__(self):
		Config.__init__(self)

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		#self.visible_sprites = pygame.sprite.Group()
		self.visible_sprites = YSortCameraGroup()
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
					Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'Graphics/rock.png',self.TILE_ID)
				#if col == ' ':
			#		Player((x,y),[self.visible_sprites])

	def run(self, player):
		# update and draw the game
		"""self.visible_sprites.custom_draw(self.player)"""
		self.visible_sprites.custom_draw(player)
		# Since theres nothing to update this line does nothing.
		"""self.visible_sprites.update()"""
		#debug(self.player.direction)
		#self.visible_sprites.update()
		

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

	def custom_draw(self, player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width 
		self.offset.y = player.rect.centery - self.half_height 

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

# What we need to do is move everything else (including other players) relative towards the player.
# Pretty much all the sprites need to be updated here but we need to find a better way in order to draw
# the tiles to move and the player + the other players. the player should stay neutral in the middle.
# but we need to get all players too. Good luck future me. 🙏 Good bye 22:23 04/08/2023