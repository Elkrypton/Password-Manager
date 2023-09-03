


# import pandas as pd 
from database import ProcessInformation, AccessData, GetData
from utils import CryptTools
import traceback
from collections import OrderedDict
###we may have to adjust the program dto actually retrieve the data based on the provided key



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
	

	# def save_to_file(self):
	# 	headers = ['email','password',','website']
	# 	hashed = Encrypt(self.password.encode(),self.key)
	# 	rows = [self.email,self.password,hashed,self.website]
	# 	filename = 'localfiles/Passwords.csv'
	# 	with open(filename,'a',newline="") as f:
	# 		writer = csv.writer(f)
	# 		writer.writerow(headers)
	# 		writer.writerow(rows)
	# 		f.close()


# def ShowPasswords():

# 	filename ='localfiles/Passwords.csv'
# 	rows = []
# 	with open(filename,'r',newline="") as f:
# 		reader = csv.reader(f,delimiter='|')
# 		header = next(reader)
# 		for row in reader:
# 			rows.append(row)
# 	print(header)
# 	print(rows)


# def pandas_view():
# 	filename = 'localfiles/Passwords.csv'
# 	try:

# 		File = pd.read_csv(filename)
# 		print(File[['email','password','hashed','website']])
# 	except:
# 		print("[!] -_- there are no passwords here babe, create a new file with the store password option.")

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
		hashed = info.hashed.decode()
		password = CryptTools(hashed).Decrypt()
		
	table_data = [(str(info.id), info.website, info.email, password) for info in data]
	print(table_data)
	pretty_print_table([("ID", "WEBSITE","EMAIL","HASHED")] + table_data)


def main(): 

	print("""
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




# 	while True:


# 		print("""

# .------..------..------..------..------..------.
# |C.--. ||H.--. ||E.--. ||E.--. ||K.--. ||S.--. |
# | :/\: || :/\: || (\/) || (\/) || :/\: || :/\: |
# | :\/: || (__) || :\/: || :\/: || :\/: || :\/: |
# | '--'C|| '--'H|| '--'E|| '--'E|| '--'K|| '--'S|
# `------'`------'`------'`------'`------'`------'


# 				1 - Store password
# 				2 - View Password


# 		""")

# 		choice = int(input("\n>>"))
# 		if choice == 1:
# 			email = input("[+] Email : ")
# 			password = input("[+] Password:")
# 			website  = input("[+] Website:")
# 			login = PasswordManager(email,password,website)
# 			login.generate_key()
# 			login.save_to_file()

# 		elif choice == 2:
# 			pandas_view()

# 		else:
# 			pass


# main()
main()

