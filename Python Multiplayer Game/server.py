import socket
from _thread import *
import pickle
from random import randint, choice
from settings import Config
from player import Player
import string

class Server(Config):
    def __init__(self):
        super().__init__()
        self.server = self.SERVER
        self.port = self.PORT
        self.players = {}
        self.connections = 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.s.bind((self.server, self.port))
        except socket.error as e:
            str(e)

        self.s.listen()
        print("Waiting for connections, Server Started")

    def create_random_string(self):
        characters = string.ascii_letters + string.digits
        return ''.join(choice(characters) for _ in range(self.ID_STRING_LENGTH))

    def return_key_value(self):
        running_loop = True
        while running_loop:
            random_string = self.create_random_string()
            if random_string not in self.players:
                running_loop = False
                return random_string

    def threaded_client(self, conn):
        key_string = self.return_key_value()
        new_player = Player(self.get_player_position()[0], self.get_player_position()[1], self.SQUARE_SIZE, self.SQUARE_SIZE, self.get_player_color())
        self.players[key_string] = new_player
        print(self.players)

        conn.send(pickle.dumps(new_player))
        running = True
        while running:
            try:
                data = pickle.loads(conn.recv(4096))
                self.players[key_string] = data

                if not data:
                    print("Player " + str(key_string) + " disconnected")
                    running = False
                else:
                    # Send the updated list of players to all clients
                    reply = self.players
                    print("Reply:", reply)

                conn.sendall(pickle.dumps(reply))
            except:
                print("Player " + str(key_string) + " lost connection")
                running = False
                break

        print("Connection Closed for Player " + str(key_string))
        del self.players[key_string]
        conn.close()

    def get_player_position(self):
        x = randint(self.SQUARE_SIZE, self.WIDTH - self.SQUARE_SIZE)
        y = randint(self.SQUARE_SIZE, self.HEIGHT - self.SQUARE_SIZE)
        return x, y

    def get_player_color(self):
        color = (randint(50, 255), randint(50, 255), randint(50, 255))
        return color

    def run(self):
        server_loop = True
        while server_loop:
            conn, addr = self.s.accept()
            self.connections += 1
            print("Connected to:", addr)
            print("There are a total of " + str(self.connections) + " connections!")

            start_new_thread(self.threaded_client, (conn,))

if __name__ == "__main__":
    server = Server()
    server.run()
