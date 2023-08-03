from socket import gethostname, gethostbyname

class Config():
    def __init__(self):
        self.HEIGHT = 500
        self.WIDTH = 500
        self.SQUARE_SIZE = 50
        self.FPS = 60
        self.HOST_NAME = gethostname()
        self.SERVER = gethostbyname(self.HOST_NAME)
        self.PORT = 5555
        self.ID_STRING_LENGTH = 15
        self.BG_COLOR = (255,255,255)
        self.DATA_SIZE = 4096

# This class is used for the client and the server.
# This means that if you are the server then you can keep this bit of code.
# But if you are not the server, but still on the same computer (assuming you have the same ipv4),
# then you will be fine as your still connecting to the server.
# Finally, you will need to change this if you are running a Client instance from another computer on the local network.
# Hope this helped. 🙏 discord: @realdl
