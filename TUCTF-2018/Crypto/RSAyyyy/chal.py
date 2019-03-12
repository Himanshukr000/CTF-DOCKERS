#!/usr/bin/env python3

import socket, sys, requests, random, binascii, modinv

from Crypto.Util import number

from _thread import *

SERVER_MODE = False # True runs server, False is stdin/out

HOST = ''
PORT = 8888

TEXT = """
               AAA               YYYYYYY       YYYYYYYYYYYYYY       YYYYYYYYYYYYYY       YYYYYYY
              A:::A              Y:::::Y       Y:::::YY:::::Y       Y:::::YY:::::Y       Y:::::Y
             A:::::A             Y:::::Y       Y:::::YY:::::Y       Y:::::YY:::::Y       Y:::::Y
            A:::::::A            Y::::::Y     Y::::::YY::::::Y     Y::::::YY::::::Y     Y::::::Y
           A:::::::::A           YYY:::::Y   Y:::::YYYYYY:::::Y   Y:::::YYYYYY:::::Y   Y:::::YYY
          A:::::A:::::A             Y:::::Y Y:::::Y      Y:::::Y Y:::::Y      Y:::::Y Y:::::Y   
         A:::::A A:::::A             Y:::::Y:::::Y        Y:::::Y:::::Y        Y:::::Y:::::Y    
        A:::::A   A:::::A             Y:::::::::Y          Y:::::::::Y          Y:::::::::Y     
       A:::::A     A:::::A             Y:::::::Y            Y:::::::Y            Y:::::::Y      
      A:::::AAAAAAAAA:::::A             Y:::::Y              Y:::::Y              Y:::::Y       
     A:::::::::::::::::::::A            Y:::::Y              Y:::::Y              Y:::::Y       
    A:::::AAAAAAAAAAAAA:::::A           Y:::::Y              Y:::::Y              Y:::::Y       
   A:::::A             A:::::A          Y:::::Y              Y:::::Y              Y:::::Y       
  A:::::A               A:::::A      YYYY:::::YYYY        YYYY:::::YYYY        YYYY:::::YYYY    
 A:::::A                 A:::::A     Y:::::::::::Y        Y:::::::::::Y        Y:::::::::::Y    
AAAAAAA                   AAAAAAA    YYYYYYYYYYYYY        YYYYYYYYYYYYY        YYYYYYYYYYYYY        
"""

INTRO = """
This challenge is designed to act as an introduction to RSA.
If you have a team member that is not already familiar with RSA,
then give this challenge to them.

For the first level, I recommend looking at 
https://simple.wikipedia.org/wiki/RSA_algorithm
but any description of the RSA algorithm will do.

Later levels will probably require further research.

Let's get started!


"""

END = """
Congratulations on finishing this introduction to RSA!
I hope this was fun and informative.

Here's your flag:\n"""

FLAG = 'TUCTF{RSA_1$_R34LLY_C00L_4ND_1MP0RT4NT_CRYPT0}'

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()


GOOD = ['Nice job!', 'Way to go!', 'Yeah! You do that RSA!', 'Ayyyyy', 'Whoop whoop!', 'That was adequate.']

BAD = ['No.', 'Wrong.', 'You can do better.', 'Inadequate.', 'Try again.']

class Part:

	response = None

	def __init__(self, conn, prompt, answers, prev_part = None):
		self.prompt = prompt
		self.answers = answers
		self.conn = conn
		self.prev_part = prev_part

	def getResponse(self):
		return self.response

	def send_prompt(self):
		if self.conn is None:
			print(self.prompt, end='')
		else:
			self.conn.send(self.prompt.encode('utf-8'))

	def send_good_response(self):
		global GOOD
		r = '\n' + random.choice(GOOD) + '\n\n'
		if self.conn is None:
			print(r, end='')
		else:
			self.conn.send(r.encode('utf-8'))

	def send_bad_response(self):
		global BAD
		r = '\n' + random.choice(BAD) + '\n\n'
		if self.conn is None:
			print(r, end='')
		else:
			self.conn.send(r.encode('utf-8'))

	def check_answer(self):
		if self.conn is None:
			data = input()
		else:
			data = self.conn.recv(1024)
			data = data.decode('utf-8')
			if not data:
				return False

		try:
			a = int(data)
		except ValueError:
			if self.conn is None:
				print('Answer should be an integer.\n', end='')
			else:
				self.conn.send('Answer should be an integer.\n'.encode('utf-8'))
			return self.check_answer()

		self.response = a
		if self.prev_part is not None:
			if a in self.answers and a != self.prev_part.getResponse():
				return True
			return False
		return a in self.answers

class Level:
	parts = []
	name = ''
	number = 0
	conn = None

	def run_level(self):
		i = 0
		if self.conn is None:
			print('\n' + self.name + '\n\n', end='')
		else:
			self.conn.send(('\n' + self.name + '\n\n').encode('utf-8'))
		while i < len(self.parts):
			part = self.parts[i]

			part.send_prompt()

			if part.check_answer():
				part.send_good_response()
				i += 1
			else:
				part.send_bad_response()
		if self.conn is None:
			print('Congratulations! You beat Level {}!\n\n'.format(self.number), end='')
		else:
			self.conn.send(('Congratulations! You beat Level {}!\n\n'.format(self.number)).encode('utf-8'))


class Level1(Level):

	def __init__(self, conn):
		self.conn = conn
		self.number = 1
		self.name = "Level 1: Calculating n"
		p = number.getPrime(32)
		q = number.getPrime(32)

		answers = [p*q,]
		self.parts = [Part(conn, "p = {}\nq = {}\nWhat is n?\n".format(p, q), answers),]

class Level2(Level):

	def __init__(self, conn):
		global WORDS
		self.conn = conn
		self.number = 2
		self.name = "Level 2: Calculating m"

		prompt = 'In order to calculate the ciphertext,\nthe message needs to be converted to an integer.\n\n'

		if conn is None:
			print(prompt, end='')
		else:
			conn.send(prompt.encode('utf-8'))

		words = [random.choice(WORDS).decode('utf-8') for i in range(5)]

		message = ' '.join(words)

		m = int(binascii.hexlify(message.encode('utf-8')), 16)

		self.parts = [Part(conn, 'message = "{}"\nWhat is m?\n'.format(message), [m,]),]

class Level3(Level):

	def __init__(self, conn):
		global WORDS
		self.conn = conn
		self.number = 3
		self.name = "Level 3: Calculating c"

		prompt = 'Now, we are going to actually calculate ciphertext.\n\n'

		if conn is None:
			print(prompt, end='')
		else:
			conn.send(prompt.encode('utf-8'))

		p = number.getPrime(32)
		q = number.getPrime(32)
		e = 65537

		n = p*q

		p1 = Part(conn, 'p = {}\nq = {}\nWhat is n?\n'.format(p, q), [n,])

		message = random.choice(WORDS)

		m = int(binascii.hexlify(message), 16)

		p2 = Part(conn, 'e = {}\nm = {}\nWhat is c?\n'.format(e, m), [pow(m, e, n),])

		self.parts = [p1,p2]

class Level4(Level):

	def __init__(self, conn):
		self.conn = conn
		self.number = 4
		self.name = "Level 4: Calculating d"

		prompt = 'In order for RSA to be asymmetrical,\nthe private exponent, d, needs to be calculated.\n\n'

		if conn is None:
			print(prompt, end='')
		else:
			conn.send(prompt.encode('utf-8'))

		p = number.getPrime(32)
		q = number.getPrime(32)
		e = 65537

		tot = (p-1) * (q-1)

		p1 = Part(conn, 'p = {}\nq = {}\nWhat is tot(n)?\n'.format(p, q), [tot,])

		d = modinv.modinv(e, tot)

		p2 = Part(conn, 'e = {}\nWhat is d?\n'.format(e), [d,])

		self.parts = [p1, p2]

class Level5(Level):

	def __init__(self, conn):
		self.conn = conn
		self.number = 5
		self.name = "Level 5: Factoring n"

		prompt = 'The easiest way to break RSA is factoring n, if it is possible.\n\n'

		if conn is None:
			print(prompt, end='')
		else:
			conn.send(prompt.encode('utf-8'))

		p = number.getPrime(32)
		q = number.getPrime(32)
		n = p * q

		p1 = Part(conn, 'n = {}\nWhat is p?\n'.format(n), [p, q])

		p2 = Part(conn, 'What is q?\n', [p, q], p1)

		self.parts = [p1, p2]

class Level6(Level):

	def __init__(self, conn):
		global WORDS
		self.conn = conn
		self.number = 6
		self.name = "Level 6: Breaking simple RSA"

		prompt = 'Now, let\'s put everything together and break RSA!\n\n'

		if conn is None:
			print(prompt, end='')
		else:
			conn.send(prompt.encode('utf-8'))

		p = number.getPrime(32)
		q = number.getPrime(32)
		n = p * q
		e = 65537

		tot = (p-1) * (q-1)

		d = modinv.modinv(e, tot)

		message = random.choice(WORDS)

		m = int(binascii.hexlify(message), 16)

		while m >= n:
			message = random.choice(WORDS)
			m = int(binascii.hexlify(message), 16)

		c = pow(m, e, n)

		p1 = Part(conn, 'c = {}\nn = {}\ne = {}\nWhat is p?\n'.format(c, n, e), [p, q])

		p2 = Part(conn, 'What is q?\n', [p, q], p1)

		p3 = Part(conn, 'What is tot(n)?\n', [tot,])

		p4 = Part(conn, 'What is d?\n', [d,])

		p5 = Part(conn, 'Finally, what is m?\n', [m,])

		self.parts = [p1, p2, p3, p4, p5]

if SERVER_MODE:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print('Socket created')

	try:
		s.bind((HOST, PORT))
	except socket.error as msg:
		print('Bind failed. Error code: ' + str(msg[0]) + ' Message ' + msg[1])
		sys.exit()

	print('Socket bind complete')

	s.listen(10)
	print('Socket now listening')

def clientthread(conn):
	try:
		conn.send((TEXT + INTRO).encode('utf-8'))

		Levels = [Level1, Level2, Level3, Level4, Level5, Level6]
		# Levels = [Level6,]

		i = 0

		for level in Levels:
			l = level(conn)
			l.run_level()

		conn.send((END + FLAG + '\n\n').encode('utf-8'))

		conn.close()
	except (BrokenPipeError, ConnectionResetError):
		pass

cont = True
while cont:
	if SERVER_MODE:
		conn, addr = s.accept()
		print('Connected with ' + addr[0] + ': ' + str(addr[1]))

		start_new_thread(clientthread, (conn,))
	else:
		print(TEXT + INTRO, end='')
		conn = None
		Levels = [Level1, Level2, Level3, Level4, Level5, Level6]

		i = 0

		for level in Levels:
			try:
				l = level(conn)
				l.run_level()
			except EOFError:
				cont = False
				break

		if cont:
			print(END + FLAG + '\n\n', end='')
			cont = False

if SERVER_MODE:
	s.close()