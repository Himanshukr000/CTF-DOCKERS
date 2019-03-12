from random import getrandbits
import SocketServer

def getPrime(k):
	x=getrandbits(k)
	while True:
		ok=1
		i=2
		while i*i<=x:
			if(x%i==0):
				ok=0
				break
			i+=1
		if ok:
			break
		else: x+=1
	return x
	
MOD = getPrime(32)
PORT = 2000

def evaluate(poly,x):
	ans=0
	for i in range(len(poly)):
		ans=ans*x+poly[i]
	return ans % MOD

flag = [ord(y) for y in open('flag.txt').read().strip()]

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.request.settimeout(15)
		self.request.sendall("Hello to the most amazing Christmas event. The X^n-Mas!\nYou can send at most 50 requests to the server.\nThe modulo is {}. Good luck!\n".format(MOD))

		for i in range(50):
			self.request.sendall("Enter a integer:")
			x=self.request.recv(2048)
			try:
				x=int(x)
				if x<0 or x>=MOD:
					self.request.sendall("Value not in range [0,{}]\n".format(MOD-1))
					break
				value = evaluate(flag,x)
			except Exception:
				ret = 'Error'
			try:
				self.request.sendall("The output is: {}\n".format(value))
			except Exception:
				break

			def finish(self):
				logger.info("%s client disconnected" % self.client_address[0])


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ == '__main__':
	server = ThreadedTCPServer(('0.0.0.0', PORT), ThreadedTCPRequestHandler)
	server.allow_reuse_address = True
	server.serve_forever()


