
from cryptography.fernet import Fernet

def Encrypt(text, key):
	return Fernet(key).encrypt(text)

def Decrypt(token,key):
	return Fernet(key).decrypt(token)
