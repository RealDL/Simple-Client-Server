import pygame
from network import Network
from settings import Config
import sys

class Client(Config):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Client")
        self.clock = pygame.time.Clock()
        self.run = True
        self.network = Network()
        self.player = self.network.getP()
        print("player: ", self.player)

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
        while self.run:
            self.clock.tick(self.FPS)
            all_players = self.network.send(self.player)

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
