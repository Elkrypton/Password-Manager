import os
from cryptography.fernet import Fernet 


class CryptTools():

        def __init__(self, text, key):
                self.text = str(text)
                self.key = self.FindKey()

        def FindKey(self):
                _file = "keys.txt"
                key = ""
                for file_ in os.listdir():
                        if os.path.exists(_file):
                                
                                content = open(file_, 'r')
                                key += content
                        else:
                                print(">> file does not exist")
                return key
        
                        
