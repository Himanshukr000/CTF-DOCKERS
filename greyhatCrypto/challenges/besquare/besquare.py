from hashlib import sha512,sha1
import random,sys,struct
import SocketServer
import base64 as b64
import os
import hmac
from time import time

password = open('password.txt','rb').read()
flag = open('flag.txt','rb').read()
N = 0x3a8e96c21536f93f9fe819d151b2114577176a6f7c05d8c3f6593d5046a54deed90c756ab121a60623f5e27c202e6c4cbf72990797fda6ea988e0d42575d4a76d2936f3bcb92eab88098fa6d5ef93d30eede6c32c8c3f1f576fb72d24bec2df08282eb3587af0a9f984af5fa4d665038e98789561f59718635c5081dd8d2025c109f980630809bb61020d8185705f224b94a7f1760a0f2d6a93fb4f3caeb9fbc408b346b97b726dedcd87f72c12f72a5f552ee2e2260ee0295d7a1013ddd778a3ce6480832e85b4e8d5389404c0884c0fa78b197afef8a156dfadae80523eb9cd9911180fb193ebeeb141f2f3f4cd682b373c3832a43875f94646a8ef2d206eb

class HandleCheckin(SocketServer.BaseRequestHandler):
	accepted = {}
	def hashToInt(self,*params):
		sha = sha512()
		for el in params:
			sha.update("%r"%el)
		return int(sha.hexdigest(), 16)

	def cryptrand(self,n = 2048):
		p1 = self.hashToInt(os.urandom(40))<<1600
		p1+= self.hashToInt(p1)<<1000
		p1+= self.hashToInt(p1)<<500
		p1+= self.hashToInt(p1)
		bitmask = ((2<<(n+1))-1)
		p1 = (p1&bitmask)
		return (p1 % N)

	def sendInt(self,toSend):
		s = hex(toSend)
		s = s[2:]
		if s[-1] =="L":
			s = s[:-1]
		self.request.sendall(s+"\n")

	def readInt(self):
		req = self.request
		leng = struct.unpack("H", req.recv(2))[0]
		if leng>520:
			req.sendall("Sorry that is too long a number\n")
			req.close()
			return None
		toRead = ""
		while len(toRead) < leng:
			toRead +=  req.recv(leng - len(toRead))
		if len(toRead) > leng:
			req.sendall("Length does not match input data size\n")
			req.close()
			return None
		return int(toRead.strip('Ll'),16)

	def checkBlacklist(self):
		foreign = self.request.getpeername()[0]
		if foreign in self.accepted:
			while(len(self.accepted[foreign]) >0 and
				self.accepted[foreign][0]<time()-600):
				del self.accepted[foreign][0]
			if len(self.accepted[foreign])>35:
				self.request.send("Too many requests too quick sorry\n")
				self.request.close()
				return False
		else:
			self.accepted[foreign] = []
		return True

	def doChallenge(self):
		req = self.request

		proof = b64.b64encode(os.urandom(12))
		req.sendall("You must first solve a puzzle, a sha1 sum ending in 24 bit's set to 1, it must be of length %s bytes, starting with %s" % (len(proof)+5, proof))
		test = req.recv(21)

		ha = sha1()
		ha.update(test)

		if(not self.checkBlacklist()):
			return False
		if (test[0:16] !=  proof or
			ha.digest()[-3:] !=  "\xff\xff\xff"):
			req.sendall("NOPE")
			req.close()
			return False

		self.accepted[self.request.getpeername()[0]].append(time())
		return True

	def getClientParams(self):
		req = self.request
		index = self.readInt()
		if index is None:
			return
		if index<2 or index>N/2:#we don't have nearly that many users, we wish we did but lets be honest ,brute force attempt
			req.sendall("Invalid nonce\n")
			req.close()
			return None
		req.sendall("Please provide your ephemeral key\n")
		cEphemeral = self.readInt()
		if cEphemeral is None:
			return None
		if cEphemeral%N ==0:
			req.sendall("Invalid ephemeral key\n")
			req.close()
			return None
		return cEphemeral,index

	def authenticate(self,index,cEphemeral,salt):
		hashToInt =  self.hashToInt
		salt = hashToInt(index)

		storedKey = pow(index, hashToInt(salt, password), N)
		multiplierSlush = 3

		sEphemeralPriv = self.cryptrand()
		sEphemeral = (multiplierSlush * storedKey +
			pow(index, sEphemeralPriv, N)) % N

		self.sendInt(salt)
		self.sendInt(sEphemeral)

		slush = hashToInt(cEphemeral, sEphemeral)
		agreedKey = hashToInt(pow(cEphemeral * pow(storedKey, slush, N), sEphemeralPriv, N))
		return agreedKey,sEphemeral

	def handle(self):
		hashToInt = self.hashToInt
		req = self.request
		if (not self.doChallenge()):
			return

		req.sendall("""Welcome to the new cryptographic authentication server. Log in or be square!

Note: passwords must contain at least one uppercase, one lowercase, and one digit. Sorry for the inconvienence but we've had problems with weak passwords lately.

To begin, please provide a randomly generated nonce.
""")

		cEphemeral,index = self.getClientParams()

		salt = self.hashToInt(index)
		agreedKey,sEphemeral = self.authenticate(index,cEphemeral,salt)

		gennedKey = hashToInt(hashToInt(N) ^ hashToInt(index), hashToInt(index), salt,
			cEphemeral, sEphemeral, agreedKey)

		check = self.readInt()

		if (check == gennedKey):
			req.sendall(flag+"\n")

		req.close()

class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ ==  "__main__":
	HOST, PORT = sys.argv[1], int(sys.argv[2])
	print 'Running on port', PORT
	server = ThreadedServer((HOST, PORT), HandleCheckin)
	server.allow_reuse_address = True
	server.serve_forever()
