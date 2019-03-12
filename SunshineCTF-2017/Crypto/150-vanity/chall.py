#!/usr/bin/env python
from pybitcoin import BitcoinPrivateKey
import random 

def read_flag(file_name):
	with open(file_name) as filein:
		print filein.read().strip()

def random_address():
	charset = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
	i = 0
	output = "1"
	while(i<33):
		output+=random.choice(charset)
		i=i+1
	return output

def run():
	intensity = 5
	
	print("The local vendor is warry to accept anynthing but bitcoin, but he only checks the first ")
	print("four characters of each address.")
	print("Can you make him think you are sending him the coins while they really go to yourself?")
	print("\n\n\n\n\n")
	
	i = 1
	while i <= intensity:
		print("Hey there! Here's my Bitcoin address:")
		#private_key = BitcoinPrivateKey()
		#target = private_key.public_key().address()
		target = random_address()
		print(target+"\n")
		
		try:
			print("Enter your private key(in hex, uncompressed): ")
			privkey_hex = int(raw_input(""), 16)
		except ValueError:
			print("That wasnt a valid key! Get out of here!")
			break
		try:
			currkey = BitcoinPrivateKey(privkey_hex, compressed=False)
			test = currkey.public_key().address()
			print("\nThat key came out to:")
			print(test+"\n")
		except:
			print("That wasn't a valid key! Get out of here!")
			break
		if(target[:4] != test[:4]):
			print("That key isn't right! Get out of here!")
			break
		
		if i < intensity:
			print("Glad the payment went through, here are your goods.")
			print("You only have %d purchases left!" % (intensity - i))
		
		i = i + 1
	if i >= intensity:
		print("Thanks for all of your payments, here's your flag:")
		read_flag("flag.txt")

if __name__ == "__main__":
	run()
