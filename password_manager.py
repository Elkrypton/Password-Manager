
#importing the modules we need to make the project.
from database import ProcessInformation, AccessData, GetData
from utils import CryptTools
import traceback
from collections import OrderedDict



#the class is responsible for managing the input and output of the user process
class PasswordManager():

	def __init__(self,website,email,password):
		self.website = website
		self.email = email
		self.password = password


	#save data to a local db file
	def SavePassword(self):
		login_info = ProcessInformation(self.website, self.email, self.password)
		try:
			login_info.add_data()

		
		except Exception as err:
			traceback.print_exc()
			print("FUNC: SAVEPASSWORD \n[!] Error encountered ! : {}".format(str(err)))
	
#This function creates a table to displat the data on the console neatly
def pretty_print_table(data):
    col_widths = [max(len(str(value)) for value in column) for column in zip(*data)]
    
    for row in data:
        print(" | ".join(f"{str(value):<{width}}" for value, width in zip(row, col_widths)))
    
    separator = "+".join("-" * (width + 2) for width in col_widths)
    print(separator)

def ShowLoginInfo():
	info = AccessData()
	table_data = [(str(login.id), login.website, login.email, login.hashed[:20]) for login in info]
	pretty_print_table([("ID","Website","Email","Hashed")] + table_data)


def GetSpecificInfo(query):
	data = GetData(query)
	for info in data:
		if type(info.hashed) == str:
			hashed = info.hashed
			password = CryptTools(hashed).Decrypt()

			
		else:
			hashed = info.hashed.decode()
			password = CryptTools(hashed).Decrypt()
		
	table_data = [(str(info.id), info.website, info.email, password) for info in data]
	pretty_print_table([("ID", "WEBSITE","EMAIL","HASHED")] + table_data)


def main(): 


	print("""


# .------..------..------..------..------..------.
# |C.--. ||H.--. ||E.--. ||E.--. ||K.--. ||S.--. |
# | :/\: || :/\: || (\/) || (\/) || :/\: || :/\: |
# | :\/: || (__) || :\/: || :\/: || :\/: || :\/: |
# | '--'C|| '--'H|| '--'E|| '--'E|| '--'K|| '--'S|
# `------'`------'`------'`------'`------'`------'

		1 - Save password
		2 - View password
		3 - Search By Website
	""")


	choice = int(input(">>:"))
	if choice == 1:
		website = input(">> Website:")
		email = input(">> Email:")
		password = input(">> Password:")
		crypt = CryptTools(password)
		hashed = crypt.Encrypt()
		login = PasswordManager(website, email, hashed)
		try:
			login.SavePassword()

		except Exception as err:
			print(">> Some shit went wrong! : {}".format(str(err)))
			traceback.print_exc()
		
	elif choice == 2:
		ShowLoginInfo()

	elif choice == 3:
		query = input(">> Website:")
		GetSpecificInfo(query)



main()

