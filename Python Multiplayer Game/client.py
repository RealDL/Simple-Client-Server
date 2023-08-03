import pygame
from network import Network
from settings import Config
from encryption import *
import sys

class Client(Config):
    def __init__(self):
        # Setting up Client
        Config.__init__(self)
        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Client")
        self.clock = pygame.time.Clock()
        self.run = True
        self.network = Network()

        # Recieve the public key from the server and player
        data = serialize_data_recieve(self.network.connect())
        key = serialize_data_recieve(data["key"])
        self.encryption = AESEncryption(key.key)
        self.player = serialize_data_recieve(self.encryption.decrypt(data['player']))

        # Print statements
        print("Received key object:",self.encryption)
        print("Received player object",self.player)

    def redraw_window(self, players):
        # win = pygame.display.get_surface()
        self.win.fill(self.BG_COLOR)

        for player_key in players:
            player = players[player_key]
            player.draw(self.win)

        pygame.display.update()

    def close(self):
        self.run = True
        pygame.quit()
        sys.exit()

    def main(self):
        # Main Client loop
        while self.run:
            self.clock.tick(self.FPS)
            player_to_send = self.encryption.encrypt(serialize_data_send(self.player))
            all_players = serialize_data_recieve(self.encryption.decrypt(self.network.send(player_to_send)))

            # Print Statements
            print("Sending player data:",self.player)
            print("Received players dictionary:",all_players)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close()

            self.player.move()
            self.redraw_window(all_players)

if __name__ == "__main__":
    client = Client()
    client.main()
