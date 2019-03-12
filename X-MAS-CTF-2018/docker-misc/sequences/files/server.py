from hashlib import md5
import string
from random import uniform,randint
import SocketServer
import requests

low = 1
high = 99999
PORT=2000
flag=open('flag.txt').read().strip()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.request.settimeout(100)

		a=''.join([chr(randint(97,122)) for i in range(16)])
		Hash=md5(a).hexdigest()[:5]
		self.request.sendall("CAPTCHA!!!\nGive a string X such that md5(X).hexdigest()[:5]={}.\n".format(Hash))
		X=self.request.recv(2048).strip()
		if(md5(X).hexdigest()[:5]==Hash):
			self.request.sendall("Ok, you can continue, go on!\n")
		else:
			self.request.sendall("You shall not pass!\n")
			return

		self.request.sendall("Hello, litlle one! This time the challenge is very random!\nYou will be asked 25 questions where you are given the first 30 terms of a random integer sequence and you will have to determine the next term of that sequence!\nLet's start!\n\n")
		i=0
		while(i<25):
			seqid = 'A0' + str(randint(low, high)).zfill(5)
			r =  requests.get('https://oeis.org/' +seqid)
			x=[int(y) for y in r.text.split('<tt>')[1].split('</tt>')[0].split(',')]
			if(len(x)>31):
				self.request.sendall('Question number {}!\nHere\'s the sequence:'.format(i+1)+'\n')
				self.request.sendall(str(x[:30])+'\n')
				self.request.sendall('input an integer:\n\n')
				rec=self.request.recv(2048).strip()
				try:
					rec=int(rec)
				except:
					self.request.sendall('Input is not an integer! Aborting.\n')
					return
				if(x[30]==rec):
					if(i<24):
						self.request.sendall('Good job, next question!\n\n')
					else:
						self.request.sendall('Yay, you did it! Here\'s your flag: {}'.format(flag))
		
				else:
					self.request.sendall('Wrong answer! Aborting.\n\n')
					return
				i+=1

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ == '__main__':
	server = ThreadedTCPServer(('0.0.0.0', PORT), ThreadedTCPRequestHandler)
	server.allow_reuse_address = True
	server.serve_forever()

