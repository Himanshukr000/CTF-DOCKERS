from hashlib import md5
import string
from random import randint
import SocketServer

PORT=2000
flag=open('flag.txt').read().strip()

class AI():
	def isWinning(self,nim):
		x=0
		for i in range(len(nim.Piles)):
			x^=nim.Piles[i]
		return x!=0
	
	def xorToWin(self,nim):
		x=0
		for i in range(len(nim.Piles)):
			x^=nim.Piles[i]
		return x

	def move(self,nim):
		if not self.isWinning(nim):
			pos=randint(0,len(nim.Piles)-1)
			while nim.Piles[pos]==0:
				pos=randint(0,len(nim.Piles)-1)
			quant=randint(1,nim.Piles[pos])
			return pos,quant
		else:
			xor=self.xorToWin(nim)
			pos=randint(0,len(nim.Piles)-1)
			while nim.Piles[pos]==0 or nim.Piles[pos]^xor>nim.Piles[pos]:
				pos=randint(0,len(nim.Piles)-1)
			print nim.Piles[pos]^xor<=nim.Piles[pos]
			return pos,nim.Piles[pos]-(xor^nim.Piles[pos])

class NIM():
	def __init__(self,piles,rng):
		self.Piles=[randint(1,rng) for i in range(piles)]
		self.sum=sum(self.Piles)
		
	def remove(self,pile,quant):
		if self.Piles[pile]<quant:
			return "Invalid move!"
		else:
			self.sum-=quant
			self.Piles[pile]-=quant
			return "Ok, valid move!"

	def finished(self):
		return self.sum==0

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

		self.request.sendall("Help Santa win this game against one of his gnomes!\nThe rules are simple, choose a non-empty pile of stone and remve from it a positive number of stones.\nThe player who takes the last stone wins!\nYou start.\n")
		ai=AI()
		nim=NIM(15,100)
		turn=0
		while not nim.finished():
			self.request.sendall("Current state of the game: {}\n\n".format(str(nim.Piles)))
			if turn%2:
				p,q=ai.move(nim)
				self.request.sendall("The gnome's move is: pile = {}, quantity = {}\n".format(p,q))
				nim.remove(p,q)
			else:
				try:
					self.request.sendall("Input the pile:\n")
					p=int(self.request.recv(2048))
					self.request.sendall("Input the quantity:\n")
					q=int(self.request.recv(2048))
					if(q<=0):
						self.request.sendall("Invalid move! Aborting!\n")
						break
					if(nim.remove(p,q)=="Invalid move!"):
						self.request.sendall("Invalid move! Aborting!\n")
						break
				except:
					self.request.sendall("Bad Input. Aborting!\n")
					break
			turn+=1
		if(turn%2==0):
			self.request.sendall("Sorry, you lost. Try again!\n")
		else: self.request.sendall("Nice one! Here's your flag: {}\n".format(flag))
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ == '__main__':
	server = ThreadedTCPServer(('0.0.0.0', PORT), ThreadedTCPRequestHandler)
	server.allow_reuse_address = True
	server.serve_forever()

