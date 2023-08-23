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
        self.player = Player([self.player_x,self.player_y],self.player_image,self.level.visible_sprites,self.level.obstacle_sprites,self.id)
        print(self.player)
        # Print statements
        print("Received key object:",self.encryption)
        print("Received player object",self.player)
        #except:
        #    self.close()

    def create_players(self, player_dict):
        # Update existing player instances and remove players that are not in player_dict
        players_to_remove = []
        for player in self.players:
            if player.id in player_dict:
                player_data = player_dict[player.id]
                player.rect.x = player_data['x']
                player.rect.y = player_data['y']
            else:
                print(f"Removing player instance with id: {player.id}")
                players_to_remove.append(player)
        
        for player in players_to_remove:
            # Removes the player from self.players list and visible_sprites
            self.players.remove(player)
            self.level.visible_sprites.remove(player)

        # Create new player instances for players not already in self.players
        for player_data in player_dict.values():
            player_ids = [player.id for player in self.players]
            if player_data['id'] not in player_ids:
                print(f"Creating new player instance with id: {player_data['id']}")
                new_player = Player(
                    [player_data['x'], player_data['y']],
                    player_data['image'],
                    self.level.visible_sprites,
                    self.level.obstacle_sprites,
                    player_data['id']
                )
                self.players.append(new_player)


        # Needs to be redesigned. Way too laggy. Insane player creation has made the program go mad.

    def redraw_window(self, all_players_dict):
        self.create_players(all_players_dict)
        # Blits the background
        self.win.fill(self.BG_COLOR)
        
        #Level for the player
        self.level.run(self.player)
        self.player.update()
        print("self.players",self.players)

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
