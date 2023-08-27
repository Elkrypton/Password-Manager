import os
from cryptography.fernet import Fernet 


class CryptTools():

        def __init__(self, text):
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
                                print("File does not exist, do you want to create it?")
                                choice = input("Yes/No")
                                if choice == "yes":
                                        self.GenerateKey()

                return key
        
        
        def GenerateKey(self):
                filename = "keys.txt"
                _key = Fernet.generate_key()
                key = _key.decode()
                with open(filename) as f:
                        f.write(key)
                
                f.close()


        def Encrypt(self):
                return Fernet(self.key).Encrypt(self.text)
        
        def Decrypt(self):
                return Fernet(self.key).Decrypt(self.text)


if __name__ == "__main__":
        text = input(">> Please provide a text to encrypt:")
        key = 