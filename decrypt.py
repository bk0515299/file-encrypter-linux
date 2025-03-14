#!/usr/bin/env python3


import os
from cryptography.fernet import Fernet


#let's find some files


files = []


for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py" or file == "README.md" or file == "LICENSE":
		continue
	if os.path.isfile(file):
		files.append(file)


print(files)



key = Fernet.generate_key()


with open("thekey.key", "rb") as key:
	secretkey = key.read()
secretphrase = "ps5"

user_phrase = input("Enter code\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb")as thefile:
			thefile.write(contents_decrypted)
		print("Your files have been decrypted")
else:
	print("Wrong")
