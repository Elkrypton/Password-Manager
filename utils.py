from cryptography.fernet import Fernet
import os, string, random

#This class Encrypts and decrypts texts based on the provided key
class CryptTools():

        def __init__(self, text):
                self.text = str(text)
                self.key = self.FindKey()

        def FindKey(self):
                _file = "keys.txt"
                key = ""
                for file_ in os.listdir():
                        if os.path.exists(_file):
                                content = open(_file, 'r')
                                key = content.read()
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
                encoded_text = bytes(self.text, encoding='utf-8')
                return Fernet(self.key).encrypt(encoded_text)
        
        def Decrypt(self):
            
                return Fernet(self.key).decrypt(self.text)

#Generates strong and unique passwords
class PasswordGenerator():
        
        def __init__(self, length=12):
                self.length=length
        
        def Generate(self):
                chars = string.ascii_letters + string.digits + string.punctuation
                try:

                        password = ''.join(random.choice(chars) for _ in range(self.length))
                
                except Exception as ex:
                        print("--ERROR : {}".format(ex))
                return password
