import socket
from _thread import *
from random import randint, choice
from settings import Config
from encryption import *
from player import Player
import string

class Server(Config):
    def __init__(self):
        # Setting up the server.
        Config.__init__(self)
        self.server = self.SERVER
        self.port = self.PORT
        self.players = {}
        self.connections = 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.encryption = AESEncryption()

        try:
            self.s.bind((self.server, self.port))
        except socket.error as e:
            str(e)

        self.s.listen()
        print("Waiting for connections, Server Started")

    def get_player_position(self):
        x = randint(self.SQUARE_SIZE, self.WIDTH - self.SQUARE_SIZE)
        y = randint(self.SQUARE_SIZE, self.HEIGHT - self.SQUARE_SIZE)
        return x, y

    def get_player_color(self):
        color = (randint(50, 255), randint(50, 255), randint(50, 255))
        return color

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
        # Generating player
        key_string = self.return_key_value()
        new_player = Player(self.get_player_position()[0], self.get_player_position()[1], self.SQUARE_SIZE, self.SQUARE_SIZE, self.get_player_color())
        self.players[key_string] = new_player
        
        # Encrypt the new_player and serializing the key_to_send
        key_to_send = serialize_data_send(self.encryption)
        encrypted_player_data = self.encryption.encrypt(serialize_data_send(new_player))
        data_to_send = serialize_data_send({'key':key_to_send,'player':encrypted_player_data})

        # Sending the serialized data (data_to_send).
        conn.send(data_to_send)
        print("Sending Player object to client:",  self.players)
        print("Sending Key Object:",self.encryption)

        # Main loop
        running = True
        while running:
            try:
                data = serialize_data_recieve(self.encryption.decrypt(conn.recv(self.DATA_SIZE)))
                self.players[key_string] = data
                print("Received:", data)

                if not data:
                    print("Player " + str(key_string) + " disconnected.")
                    running = False
                else:
                    # Send the updated list of players to all clients
                    reply = self.players
                    encrypted_reply = self.encryption.encrypt(serialize_data_send(reply))
                    print("Reply:", reply)

                conn.sendall(encrypted_reply)
            except:
                print("Player " + str(key_string) + " lost connection.")
                running = False

        print("Connection Closed for Player " + str(key_string) + ".")
        del self.players[key_string]
        conn.close()

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
