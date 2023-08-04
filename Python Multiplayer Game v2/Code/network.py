import socket
from settings import Config

class Network(Config):
    def __init__(self):
        Config.__init__(self)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = self.SERVER
        self.port = self.PORT
        self.addr = (self.server, self.port)
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(self.DATA_SIZE)
        except:
            pass

    def send(self, data):
        try:
            self.client.send(data)
            return self.client.recv(self.DATA_SIZE)
        except socket.error as e:
            print(e)