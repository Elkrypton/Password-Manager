
from utils
import csv
import pandas as pd 


###we may have to adjust the program dto actually retrieve the data based on the provided key


class PasswordManager():

	def __init__(self,email,password, website):
		self.email = email
		self.password = password
		self.website = website


	def save_to_file(self):
		headers = ['email','password',','website']
		hashed = Encrypt(self.password.encode(),self.key)
		rows = [self.email,self.password,hashed,self.website]
		filename = 'localfiles/Passwords.csv'
		with open(filename,'a',newline="") as f:
			writer = csv.writer(f)
			writer.writerow(headers)
			writer.writerow(rows)
			f.close()


def ShowPasswords():

	filename ='localfiles/Passwords.csv'
	rows = []
	with open(filename,'r',newline="") as f:
		reader = csv.reader(f,delimiter='|')
		header = next(reader)
		for row in reader:
			rows.append(row)
	print(header)
	print(rows)


def pandas_view():
	filename = 'localfiles/Passwords.csv'
	try:

		File = pd.read_csv(filename)
		print(File[['email','password','hashed','website']])
	except:
		print("[!] -_- there are no passwords here babe, create a new file with the store password option.")

def main():
	while True:


		print("""

.------..------..------..------..------..------.
|C.--. ||H.--. ||E.--. ||E.--. ||K.--. ||S.--. |
| :/\: || :/\: || (\/) || (\/) || :/\: || :/\: |
| :\/: || (__) || :\/: || :\/: || :\/: || :\/: |
| '--'C|| '--'H|| '--'E|| '--'E|| '--'K|| '--'S|
`------'`------'`------'`------'`------'`------'


				1 - Store password
				2 - View Password


		""")

		choice = int(input("\n>>"))
		if choice == 1:
			email = input("[+] Email : ")
			password = input("[+] Password:")
			website  = input("[+] Website:")
			login = PasswordManager(email,password,website)
			login.generate_key()
			login.save_to_file()

		elif choice == 2:
			pandas_view()

		else:
			pass


main()
