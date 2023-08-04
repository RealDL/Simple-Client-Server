import pygame
from network import Network
from settings import Config
from encryption import *
import sys
from level import Level
from debug import debug
from player import Player

class Client(Config):
    def __init__(self):
        # Setting up Client
        Config.__init__(self)
        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Client")
        self.clock = pygame.time.Clock()
        self.run = True
        self.level = Level()
        self.players = []
        # Recieve the public key from the server and player

        # Floor
        self.floor_surf = pygame.image.load('Graphics/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        
        self.network = Network()
        #try:
        data = serialize_data_recieve(self.network.connect())
        key = serialize_data_recieve(data["key"])
        self.encryption = AESEncryption(key)
        self.player_info = serialize_data_recieve(self.encryption.decrypt(data['player']))
        self.player_x = self.player_info['x']
        self.player_y = self.player_info['y']
        self.player_image = self.player_info['image']
        self.id = self.player_info['id']
        #print(self.player_x,self.player_y,self.player_image)
        self.player = Player([self.player_x,self.player_y],self.player_image,[self.level.visible_sprites],self.level.obstacle_sprites)
        print(self.player)
        # Print statements
        print("Received key object:",self.encryption)
        print("Received player object",self.player)
        #except:
        #    self.close()

    def create_players(self,player_dict):
        self.players = []
        self.temp_player = None
        for dict in player_dict.values():
            if not dict['id'] == self.id:
                temp_player = Player([dict['x'],dict['y']],dict['image'],[self.level.visible_sprites],self.level.obstacle_sprites)
                self.players.append(temp_player)

    def redraw_window(self, all_players_dict):
        self.create_players(all_players_dict)
        # Blits the background
        self.win.fill(self.BG_COLOR)
        self.win.blit(self.floor_surf,self.floor_rect)
        
        #Level for the player
        self.level.run()

        # Debug for the screen / update etc
        debug([self.player.rect.x, self.player.rect.y])
        pygame.display.update()
        self.clock.tick(self.FPS)

    def close(self):
        self.run = True
        pygame.quit()
        sys.exit()

    def main(self):
        # Main Client loop
        while self.run:
            player_dict = {'x':self.player.rect.x,'y':self.player.rect.y,'image':self.player_image,'id':self.id}
            player_encrypted_dict = self.encryption.encrypt(serialize_data_send(player_dict))
            all_players_dict = serialize_data_recieve(self.encryption.decrypt(self.network.send(player_encrypted_dict)))
            print("ALL DICT",all_players_dict)
            

            # Print Statements
            print("Sending player data:",player_dict)
            print("Received players dictionary:",all_players_dict)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close()

            self.redraw_window(all_players_dict)

if __name__ == "__main__":
    client = Client()
    client.main()
