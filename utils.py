import os
from cryptography.fernet import Fernet 


class CryptTools():

        def __init__(self, text):
                self.text = bytes(text, encoding='utf-8')
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
                return Fernet(self.key).encrypt(self.text)
        
        def Decrypt(self):
            
                return Fernet(self.key).decrypt(self.text)

if __name__ == "__main__":
    print("""1 - Encryption
            2 - Decryption"""
            )
    
    answer = int(input(">>:"))
    if answer == 1:
        text = input("[+] Content:")
        encrypt = CryptTools(text)
        print(encrypt.Encrypt())
    elif answer == 2:
        token = input(">> Provide token:")
        decrypt = CryptTools(token)
        print(decrypt.Decrypt())

