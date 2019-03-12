from hashlib import md5
import string
from random import uniform,randint
import SocketServer

PORT=2000
flag=open('flag.txt').read().strip()

class Guesser():
	def __init__(self,points,YLow,YHigh,XLow,XHigh):
		self.Oy=[(YLow+YHigh)/2]+[uniform(float(YLow),float(YHigh)) for i in range(points)]+[(YLow+YHigh)/2]
		self.Ox=[XLow-1]+sorted([uniform(XLow,XHigh) for i in range(points)])+[XHigh+1]
	
	def evalPoint(self,x):
		seq=0
		while(self.Ox[seq+1]<=x):
			seq+=1
		startOy=self.Oy[seq]
		endOy=self.Oy[seq+1]
		startOx=self.Ox[seq]
		endOx=self.Ox[seq+1]
		y=startOy+(endOy-startOy)*((x-startOx)/(endOx-startOx))
		return y

	def getMaximum(self):
		return max(self.Oy)

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.request.settimeout(20)

		a=''.join([chr(randint(97,122)) for i in range(16)])
		Hash=md5(a).hexdigest()[:5]
		self.request.sendall("CAPTCHA!!!\nGive a string X such that md5(X).hexdigest()[:5]={}.\n".format(Hash))
		X=self.request.recv(2048).strip()
		if(md5(X).hexdigest()[:5]==Hash):
			self.request.sendall("Ok, you can continue, go on!\n")
		else:
			self.request.sendall("You shall not pass!\n")
			return

		Steps=501
		LowY,HighY,LowX,HighX=randint(-20,-10),randint(30,50),randint(-50,-10),randint(100,150)
		self.request.sendall("This Christmas' dilemma is:\nGiven a random function defined in range ({}, {}) find the global maximum of the function!\nYou can send at most {} queries including guesses.\nThe guessed value must be equal to the real answer up to 2 decimals.\n\n".format(LowX,HighX,Steps))
		func=Guesser(15,float(LowY),float(HighY),float(LowX),float(HighX))
	
		for i in range(Steps):
			self.request.sendall("Choose your action:\n[1] Query the value of the function at some point\n[2] Guess the global maximum\n\n")
			try:
				choice = int(self.request.recv(2048))
				if(choice==1):
					self.request.sendall("Enter a float: ")
					inp=float(self.request.recv(2048))
					if(inp<LowX or inp>HighX):
						self.request.sendall("Value not in given range. Aborting!\n")
						break
					out=func.evalPoint(inp)
					self.request.sendall("f({}) = {}\n".format(inp,out))
				elif(choice==2):
					self.request.sendall("Enter your guess: ")
					inp=float(self.request.recv(2048))
					if(abs(inp-func.getMaximum())<0.01):
						self.request.sendall("Congratulations! Here's your flag!\n {}\n".format(flag))
					else:
						self.request.sendall("Nope, that's quite far away from the real answer.\n")
				else:
					self.request.sendall("Input invalid. Aborting!\n")
					break
			except:
				self.request.sendall("Input invalid. Aborting!\n")
				break

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ == '__main__':
	server = ThreadedTCPServer(('0.0.0.0', PORT), ThreadedTCPRequestHandler)
	server.allow_reuse_address = True
	server.serve_forever()

