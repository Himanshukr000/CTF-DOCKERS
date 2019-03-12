import discord, platform, asyncio, random
import json, requests, subprocess, os
from threading import Timer

#RUN WITH SUDO.
#REMOVE ALL R/W/X ACCESS.

client = discord.Client()
token = "NTE5NTgyNjcxMTM1ODM0MTEy.Duhbjw.p3u0N1t89FY74uVq3L6P8bLPHic"

@client.event
async def on_ready():
	print('Beep Boop. Connected!\nName is: ' + client.user.name)
	await client.change_presence(game=discord.Game(name='>Say help<'))

headerjoke = ['Initiating Jokes module...', 'Running Program... Joke!', 'Executing Humor.', 'Beep. Humor online.']
headerglitch = ['**CRANK**\nWhat are you doing?', '**CLANG!**\nWhat was that?', '**BAD INPUT**\nSorry for the inconvenience!']
deps = ['randdev@santa.com', 'toyfactory@santa.com', 'weaponsilo@santa.com', 'commandcenter@santa.com', 'test@santa.com', 'LOLOLOL@santa.com']

flag = "X-MAS{Wh0_Kn3W_4_H3lp3r_M3ch4gN0m3_W0uLd_b3_S0_vULN3R4bL3}"

header = """MechaGnome **v1.0** :hammer_pick: 
_Santa's #1 Galvanized Helper Gnome_

"""

helpmsg = """MechaGnome **#9926** Control panel. You can execute the following commands:
- **help** - Displays this message.
- **joke** - Jokes in case of emergency.
- **add** - Add the numbers x and y together. Used to test MechaGnome's internal ALU.
	_x_ - First Operand
	_y_ - Second Operand
- **list** - List Departments
- **sendletter** - Send an electronic letter to another department.
	 _address@santa.com_ - Target Address
	 _message_ - Message to Send
- **restart** - Restart MechaGnome, recovering it from any corrupted state.
"""

def demote(user_uid, user_gid):
	"""Pass the function 'set_ids' to preexec_fn, rather than just calling
	setuid and setgid. This will change the ids for that subprocess only"""

	def set_ids():
		os.setgid(user_gid)
		os.setuid(user_uid)

	return set_ids

solves = {} #Solver Accounts Dict

@client.event
async def on_message(message):
	try:
		if message.author == client.user: #Ignore own messages
			return
		
		if (message.server.name == "X-MAS CTF 2018"):
			return

		inp = message.content
		printer = header
		
		if (message.author in solves):
			state = "FUNCTIONAL"
		else:
			state = "CORRUPTEd?"
		
		printer += "Current State: __**" + state + "**__\n\n"
		
		interacted = 0
		
		if (inp == 'help'):
			interacted = 1
			printer += helpmsg
		elif (inp == 'joke'):
			interacted = 1
			r = requests.get("https://safe-falls-22549.herokuapp.com/random_joke")
			joke = json.loads(r.text)
			printer += random.choice(headerjoke) + "\n\n"
			printer += "**" + joke['setup'] + "**\n"
			printer += "_" + joke['punchline'] + "_"
		elif (inp[:3] == 'add'):
			interacted = 1
			try:
				inp = inp.split()
				num1 = int(inp[1])
				num2 = int(inp[2])
				
				printer += str(num1) + " + " + str(num2) + " = " + str(num1 + num2)
			except:
				printer += random.choice(headerglitch) + '\n\n'
				printer += 'Correct Usage: **add _52_ _10_**'
		elif (inp == 'list'):
			interacted = 1
			printer += "Current Departments:\n"
			for dep in deps:
				printer += "- _" + dep + "_" + '\n'
		elif (inp[:10] == 'sendletter'):
			interacted = 1
			inp = inp[11:]
			if (inp.find('>') != -1 or inp.find('<') != -1 or inp.find('|') != -1 or inp.find('&') != -1 or len(inp.split()) < 2):
				printer += random.choice(headerglitch) + '\n\n'
				printer += 'Correct Usage: **sendletter _address@santa.com_ _message_**'
			else:
				handle = subprocess.Popen(["/bin/sh", "-c", "echo " + ' '.join(inp.split()[1:])], shell = False, stdout=subprocess.PIPE, preexec_fn=demote(1000, 1000))
				try:
					handle.wait(2) #2 seconds timeout
					stdout = str(handle.stdout.read())[2:-1]
				except subprocess.TimeoutExpired:
					handle.kill()
					stdout = "TIMEOUT!\nBEEEEEEEEEEEEP."
				
				msg = stdout.replace("\\n", '\n')
				
				if (len(msg) > 1800):
					printer += "The message is too long be sent."
				else:
					printer += "Sent the following message:\n"
					printer += "```" + msg + "```"
					printer += "\nTo The following Address: **" + inp.split()[0] + "**"
		
		elif (inp[:7] == "restart"):
			interacted = 1
			inp = inp[8:]
			if (inp == 'XJACO-10U4C-C091U-VNOAC-J2QCS'):
				printer += "Restarting...\n"
				printer += "**Nice work!** Flag: `" + flag + "`"
				solves[message.author] = 1
			else:
				printer += "Please supply the correct restart codes.\n"
				printer += "Correct Usage: **restart _XXXXX-XXXXX-XXXXX-XXXXX-XXXXX_**"
			
		elif (inp == "gabygandakul"): #Don't Question
			interacted = 1
			printer += "Ok: https://www.youtube.com/watch?v=mOYZaiDZ7BM"
		
		if (interacted == 1):
			await client.send_message(message.channel, printer)
	except Exception as e:
		print (e)
client.run(token)
