#!/usr/bin/python

import socket
import random
import threading

IP = '0.0.0.0'
PORT = 2000
BUFF = 1024
user_lives = 0

intro = "Hello! My name is John Athan. I am Santa's right hand. Unfortunately, the Christmas is in danger. The reindeers have been trapped behind a door that requires some sort of username and password combination. Your mission, should you choose to accept it, is to help me solve some tasks and save the Christmas. If successful, you will be rewarded with a lovely flag.\n\n You have 3 lives. Good luck! \n\n"

end_game_str = "You did it! You saved the Christmas! You may now go solve some more challenges. As promised, here is your flag:\n"

game_over_str = "You lost. Christmas is lost. :( \n"
move_str = "Congrats! Moving to the next task... \n\n"

level1_str = "If you want me you'll have to share me but if you share me I will be gone. What am I?(one word)\n"

level2_str1 = "While you were struggling with that riddle I managed to extract some hashes, but triggered an alarm. I don't know much about them. They are 14 characters long and all of them contain the word 'stealer' and 7 digits. All the digits are placed after the word or before the word. The hash for the word 'admin' is -5290733415256081176 \nYou only have 60 seconds. I'm validating the strings as you send them so any mistake is fatal. Send the usernames, one per line. Here's an example:\n"
level2_str2 = "Anyway here are the hashes:\n"

level3_str = "Ok... I feel we're getting closer. I now need you to tell me how many reindeers are in this image.\n https://pasteboard.co/HRfn1ys.jpg \n"

level4_str = "Nicely done! You might actually have a shot at saving the Christmas. I have another image for you to analyze, but I'm a bit confused. I need a password so I can see where the reindeers are trapped at.\n https://pasteboard.co/HRwM0jU.png \n"

level5_str = "We're finally here. Behind this door that you are unable to see are Santa's reindeers. Give me the password and we shall save the Christmas. \n https://pasteboard.co/HRyG0yE.png \n"


#Open Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(5)
print "[*] Listening on %s:%d" % (IP, PORT)

#Generate Random Hashes
def gen_user():
	x = random.randint(1, 3)
	user = ""	

	for i in range(7):
		user += str(random.randint(0,9))
	
	if(x == 1):
		user += "stealer"
	else:
		user = "stealer" + user
	
	return user

#Print Flag
def give_flag(client, addr, user_lives):
	client.send(end_game_str)

	name = "flag.txt"
	file = open(name, "r")
	
	for line in file:
		client.send(str(line))
	client.send("\n\n Best of luck!")	

	client.close()

#Level5
def level5(client, addr, user_lives):
	client.send(level5_str)
	passwd = "this_is_not_a_red_herring"
	answer = ""

	while user_lives > 0:
		answer = ""
		answer = str(client.recv(BUFF))[:-1]
		#print "Received: " + answer
		
		if answer == passwd:
			give_flag(client, addr, user_lives)
			return
		else:
			user_lives -= 1
			outp = "\nThe answer is wrong. You have " + str(user_lives) + " lives left\n"
                        client.send(outp)
		
		client.send(game_over_str)
		client.close()	

#Level4
def level4(client, addr, user_lives):
	client.send(level4_str)
	passwd = "sternocleidomastoidian"
	answer = ""	

	while user_lives > 0:
		answer = ""
		answer = str(client.recv(BUFF))[:-1]
		#print "Received " + answer
		#print "Compare  " + passwd 		

		if answer == passwd:
			client.send(move_str)
			level5(client, addr, user_lives)
			return
		else:
			user_lives -= 1
			outp = "\nThe answer is wrong. You have " + str(user_lives) + " lives left\n"
			client.send(outp)

	client.send(game_over_str)
	client.close()
		
#Level3
def level3(client, addr, user_lives):
	#17 reindeers
	#https://pasteboard.co/HRfn1ys.jpg

	client.send(level3_str)
	modulo = random.randint(1e14 + 1, 1e16)
	client.send("You should send me (no_of_reindeers * (666 013)^3)  %  " + str(modulo) + "\n")
	
	while user_lives > 0:
		no = int(client.recv(BUFF))
		#print "Received " + str(no)
		if no == (17 * (666013**3)) % modulo:
			client.send(move_str)
			level4(client, addr, user_lives)
			return
		else:
			user_lives -= 1	
			outp = "\nThe answer is wrong. You have " + str(user_lives) + " lives left\n"
			client.send(outp)
	
	client.send(game_over_str)
	client.close()	
#Level2
def level2(client, addr, user_lives):
	client.send(level2_str1)
	#client.send("admin " + str(hash("admin")) + '\n') 
	client.send(level2_str2)
	client.settimeout(60.0)	

	users = [None] * 11
	for i in range(1, 11):
		user = gen_user()
		users[i] = user

		#print user
		#print hash(user)
		#print ""
			
		client.send(str(hash(user)) + '\n')

	for i in range(1, 11):
		user = str(client.recv(BUFF))[:-1]
		
		if(users[i] != user):
			client.send(game_over_str)
			client.close()	
	
	client.settimeout(None)
	client.send(move_str)
	level3(client, addr, user_lives)

#Level1
def level1(client, addr, user_lives):
	
	client.send(level1_str)
	request = client.recv(BUFF)
    #print "[*] Received the following request from %s:%d:   %s" % (addr[0], addr[1], request)
	prel = str(request).lower()[:-1]
	
	if prel == "secret":	
		client.send(move_str)
		level2(client, addr, user_lives)
		return
	else:
		user_lives -= 1
		
		if(user_lives != 0):
			outp = "\nThe answer is wrong. You have " + str(user_lives) + " lives left\n"
			client.send(outp)
			level1(client, addr, user_lives)
		else:
			client.send(game_over_str)
			client.close()
		 
#Main Function
def handle_client(client, addr):
	user_lives = 3
	client.send(intro)

	level1(client, addr, user_lives)

#Handle Incoming Connections
while True:
    client, addr = server.accept()
    print "[*] Incoming connection from %s:%d" % (addr[0], addr[1])

    client_handler = threading.Thread(target = handle_client, args = (client, addr,))
    client_handler.start()
