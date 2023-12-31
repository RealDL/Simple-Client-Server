from socket import gethostname, gethostbyname
from logger import *
import pickle

logger.debug("RealDL Settings Code.")

class Config():
    def __init__(self):
        self.HEIGHT = 720
        self.WIDTH = 1280
        self.SQUARE_SIZE = 64
        self.BITS = 256
        self.FPS = 60
        self.HOST_NAME = gethostname()
        self.SERVER = gethostbyname(self.HOST_NAME)
        self.PORT = 5555
        self.ID_STRING_LENGTH = 15
        self.BG_COLOR = (50,220,20)
        self.DATA_SIZE = 4096
        self.SMALL_DATA = 32
        self.ENCRYPTION_DATA_SIZE = 1024
        self.TILESIZE = 64
        self.TILE_ID = 'Tile'
        self.WORLD_MAP = [
        ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ','x',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ','x',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ','x','x','x',' ',' ',' ',' ',' ','x',' ',' ',' ','x',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x','x',' ',' ','x','x',' ',' ',' ',' ',' ',' ','x',' ',' ',' ','x',' ','x'],
        ['x',' ',' ','x','x','x','x','x',' ',' ',' ','x','x',' ',' ','x','x',' ',' ',' ',' ',' ',' ','x',' ',' ',' ','x',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ','x',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
        ]
        
    def serialize(self, data):
        try:
            return pickle.dumps(data)
        except pickle.PicklingError as Error:
            logger.error(f"Failed to pickle data: {Error}")
    
    def unserialize(self, data):
        try:
            return pickle.loads(data)
        except pickle.UnpicklingError as Error:
            logger.error(f"Failed to unpickle data: {Error}")

# This class is used for the client and the server.
# This means that if you are the server then you can keep this bit of code.
# But if you are not the server, but still on the same computer (assuming you have the same ipv4) then you will be fine.
# You will need to change this if you are running a Client instance from another computer.