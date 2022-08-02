from ftplib import FTP
from os import path
connect = input("adress of your server ")
ftp = FTP(connect)
user = input("USER: (Default anonymous) ")
if user == " ":
	user = "anonymous"
password = input("PASSWORD: (Default anonymous@)")
if password == " ":
	password = "anonymous@"
ftp.login(user , password )
ftp.retrlines('LIST')

class operation:






	def nextdir():
		nex = input("name of the next directory ") 
		ftp.cwd(nex)
		ftp.pwd()
		ftp.retrlines('LIST')

	def changedir():
		cwd = input("path ")
		ftp.cwd(cwd)
		ftp.pwd()
		ftp.retrlines('LIST')

	def savefile():
		save = input("name of your file? ")
		with open(save, 'wb') as f:
			ftp.retrbinary('RETR ' + save, f.write)

	#def uploadfile():


	

	while (True):
		quest = input("save , next dir, changedir,   ")
		if quest == "save":
			savefile()
		if quest == "next dir":
			nextdir()
		if quest == "changedir":
			changedir()

