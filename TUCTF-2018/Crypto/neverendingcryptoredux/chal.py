#!/usr/bin/env python3

import socket, sys, requests, random, binascii, modinv, time, os

from select import select

from abc import ABC, abstractmethod

from Crypto.Util import number

from _thread import *

SERVER_MODE = False # True runs server, False is stdin/out

HOST = ''
PORT = 8888

NUMBER_OF_ROUNDS = 50

VIGENERE_KEY = "TUCTF"

VIGENERETWO_KEY = "HAVEFUN"

TIMEOUT = 3


INTRO = """
Welcome to the Crypto that never ends!

I hope you're ready to stay a while.


"""

END = """
Congratulations on ending what was never ending!

Here's your flag:\n"""

FLAG = 'TUCTF{CRYPT0_D03$NT_R34LLY_3V3R_3ND}'

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()


GOOD = ['Nice job!', 'Way to go!', 'Yeah! You do that Crypto!', 'Ayyyyy', 'Whoop whoop!', 'That was adequate.']

BAD = ['No.', 'Wrong.', 'You can do better.', 'Inadequate.', 'Try again.']

class Ciphers:

	@staticmethod
	def Morse(s):
		MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
		                    'C':'-.-.', 'D':'-..', 'E':'.', 
		                    'F':'..-.', 'G':'--.', 'H':'....', 
		                    'I':'..', 'J':'.---', 'K':'-.-', 
		                    'L':'.-..', 'M':'--', 'N':'-.', 
		                    'O':'---', 'P':'.--.', 'Q':'--.-', 
		                    'R':'.-.', 'S':'...', 'T':'-', 
		                    'U':'..-', 'V':'...-', 'W':'.--', 
		                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
		                    '1':'.----', '2':'..---', '3':'...--', 
		                    '4':'....-', '5':'.....', '6':'-....', 
		                    '7':'--...', '8':'---..', '9':'----.', 
		                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
		                    '?':'..--..', '/':'-..-.', '-':'-....-', 
		                    '(':'-.--.', ')':'-.--.-'}
		o = ' '.join([MORSE_CODE_DICT[c] for c in s])
		return o

	@staticmethod
	def Caesar(s, k):
		o = ''
		k = k % 26
		for c in s:
			c = chr(((ord(c) - ord('A')) + k) % 26 + ord('A'))
			o += c
		return o

	@staticmethod
	def Rot13(s):
		return Ciphers.Caesar(s, 13)

	@staticmethod
	def FlipMorse(s):
		o = ''
		for c in s:
			if c == '-':
				o += '.'
			elif c == '.':
				o += '-'
			else:
				o += ' '
		return o

	@staticmethod
	def Matrix(s):
		o = ''
		for i in range(3):
			o += s[i::3]
		return o

	@staticmethod
	def Vigenere(s, k):
		ki = [(ord(c) - ord('A')) for c in k]
		o = ''
		for i in range(len(s)):
			o += chr(((ord(s[i]) - ord('A')) + ki[i % len(ki)]) % 26 + ord('A'))
		return o

class Part:

	response = None

	def __init__(self, conn, prompt, answer, prev_part = None):
		self.prompt = prompt
		self.answer = answer
		self.conn = conn
		self.prev_part = prev_part

	def getResponse(self):
		return self.response

	def send_prompt(self):
		if self.conn is None:
			sys.stdout.write(self.prompt)
			sys.stdout.flush()
		else:
			self.conn.send(self.prompt.encode('utf-8'))

	def send_good_response(self):
		global GOOD
		r = '\n' + random.choice(GOOD) + '\n\n'
		if self.conn is None:
			sys.stdout.write(r)
			sys.stdout.flush()
		else:
			self.conn.send(r.encode('utf-8'))

	def send_bad_response(self):
		global BAD
		r = '\n' + random.choice(BAD) + '\n\n'
		if self.conn is None:
			sys.stdout.write(r)
			sys.stdout.flush()
		else:
			self.conn.send(r.encode('utf-8'))

	def check_answer(self):
		global TIMEOUT
		if self.conn is None:
			rlist, _, _ = select([sys.stdin], [], [], TIMEOUT)
			if rlist:
				data = sys.stdin.readline()
			else:
				timeoutfunc()

			data = data.rstrip('\n').upper()
		else:
			data = self.conn.recv(1024)
			data = data.decode('utf-8')[:-1]
			if not data:
				return False

		a = data
		self.response = data
		if self.prev_part is not None:
			if a == self.answer and a != self.prev_part.getResponse():
				return True
			return False
		return a == self.answer

def check_word(word):
	for c in word:
		o = ord(c)
		if o < ord('A') or o > ord('Z'):
			return False
	return True

def timeoutfunc():
	sys.stdout.write('Too slow!\n')
	sys.stdout.flush()
	sys.exit(0)

class Level(ABC):
	parts = []
	name = ''
	number = 0
	conn = None

	@abstractmethod
	def cipher(self, word):
		return word

	def gen_parts(self):
		global NUMBER_OF_ROUNDS
		global WORDS
		self.parts = []
		for i in range(NUMBER_OF_ROUNDS):
			word = random.choice(WORDS).decode('utf-8').upper()
			while not check_word(word) or len(word) < 5:
				word = random.choice(WORDS).decode('utf-8').upper()
			ciphertext = self.cipher(word)
			self.parts.append(Part(conn, 'Decrypt {}\n'.format(ciphertext), word))

	def run_level(self):
		global TIMEOUT
		i = 0
		if self.conn is None:
			sys.stdout.write('\n' + self.name + '\n\n')
			sys.stdout.flush()

			sys.stdout.write('Give me text:\n')
			sys.stdout.flush()
			rlist, _, _ = select([sys.stdin], [], [], TIMEOUT)
			if rlist:
				data = sys.stdin.readline()
			else:
				timeoutfunc()

			data = data.rstrip('\n').upper()

			sys.stdout.write('{} encrypted is {}\n\n'.format(data, self.cipher(data)))
			sys.stdout.flush()
		else:
			self.conn.send(('\n' + self.name + '\n\n').encode('utf-8'))
			self.conn.send('Give me text:\n'.encode('utf-8'))
			data = self.conn.recv(1024)
			data = data.decode('utf-8').upper()

			self.conn.send('{} encrypted is {}\n\n'.format(data, self.cipher(data).encode('utf-8')))
		while i < len(self.parts):
			part = self.parts[i]

			part.send_prompt()

			if part.check_answer():
				part.send_good_response()
				i += 1
			else:
				part.send_bad_response()
		if self.conn is None:
			sys.stdout.write('Congratulations! You beat Level {}!\n\n'.format(self.number))
			sys.stdout.flush()
		else:
			self.conn.send(('Congratulations! You beat Level {}!\n\n'.format(self.number)).encode('utf-8'))

class Level0(Level):

	def cipher(self, word):
		return Ciphers.Morse(word)

	def __init__(self, conn):
		self.conn = conn
		self.number = 0
		self.name = "Level 0"

class Level1(Level):

	def cipher(self, word):
		return Ciphers.Morse(Ciphers.Rot13(word))

	def __init__(self, conn):
		self.conn = conn
		self.number = 1
		self.name = "Level 1"

class Level2(Level):

	def cipher(self, word):
		return Ciphers.FlipMorse(Ciphers.Morse(word))

	def __init__(self, conn):
		self.conn = conn
		self.number = 2
		self.name = "Level 2"

class Level3(Level):

	def cipher(self, word):
		return Ciphers.Morse(Ciphers.Matrix(word))

	def __init__(self, conn):
		self.conn = conn
		self.number = 3
		self.name = "Level 3"

class Level4(Level):

	def cipher(self, word):
		return Ciphers.Morse(Ciphers.Rot13(Ciphers.Matrix(word)))

	def __init__(self, conn):
		self.conn = conn
		self.number = 4
		self.name = "Level 4"

class Level5(Level):

	def cipher(self, word):
		return Ciphers.FlipMorse(Ciphers.Morse(Ciphers.Rot13(Ciphers.Matrix(word))))

	def __init__(self, conn):
		self.conn = conn
		self.number = 5
		self.name = "Level 5"

class Level6(Level):

	def cipher(self, word):
		global VIGENERE_KEY
		return Ciphers.Morse(Ciphers.Vigenere(word, VIGENERE_KEY))

	def __init__(self, conn):
		self.conn = conn
		self.number = 6
		self.name = "Level 6"

class Level7(Level):

	def cipher(self, word):
		global VIGENERETWO_KEY
		return Ciphers.FlipMorse(Ciphers.Morse(Ciphers.Matrix(Ciphers.Vigenere(word, VIGENERETWO_KEY))))

	def __init__(self, conn):
		self.conn = conn
		self.number = 7
		self.name = "Level 7"

		if conn is None:
			sys.stdout.write('You\'re good! But are you good enough\nto beat this FINAL CHALLENGE?!!!!\n\n')
			sys.stdout.flush()
		else:
			conn.send('You\'re good! But are you good enough\nto beat this FINAL CHALLENGE?!!!!\n\n'.encode('utf-8'))

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
		conn.send((INTRO).encode('utf-8'))

		Levels = [Level0, Level1, Level2, Level3, Level4, Level5, Level6, Level7]

		for level in Levels:
			l = level(conn)
			l.gen_parts()
			l.run_level()

		conn.send((END + FLAG + '\n\n').encode('utf-8'))

		conn.close()
	except (BrokenPipeError, ConnectionResetError):
		pass
	except socket.timeout:
		conn.send('Too slow!\n'.encode('utf-8'))

cont = True
while cont:
	if SERVER_MODE:
		conn, addr = s.accept()
		print('Connected with ' + addr[0] + ': ' + str(addr[1]))
		conn.settimeout(TIMEOUT)

		start_new_thread(clientthread, (conn,))
	else:
		try:
			sys.stdout.write(INTRO)
			sys.stdout.flush()
			conn = None
			Levels = [Level0, Level1, Level2, Level3, Level4, Level5, Level6, Level7]

			for level in Levels:
				try:
					l = level(conn)
					l.gen_parts()
					l.run_level()
				except EOFError:
					cont = False
					break

			if cont:
				sys.stdout.write(END + FLAG + '\n\n')
				sys.stdout.flush()
				cont = False
		except KeyboardInterrupt:
			sys.stdout.write('\n')
			sys.stdout.flush()
			sys.exit(0)

if SERVER_MODE:
	s.close()