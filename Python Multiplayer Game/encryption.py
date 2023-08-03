import pickle
from cryptography.fernet import Fernet

class AESEncryption:
    def __init__(self,key=None):
        if key:
            self.key = key
        else:
            self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher.encrypt(data)

    def decrypt(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data)
    
def serialize_data_send(data):
    return pickle.dumps(data)
    
def serialize_data_recieve(data):
    return pickle.loads(data)
