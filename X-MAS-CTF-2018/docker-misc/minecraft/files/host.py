import SocketServer as ss
import sys, subprocess, time

whitelist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()+-=\n'

class ThreadedTCPRequestHandler(ss.BaseRequestHandler):
	def handle(self):
		try:
			print ("New connection from " + str(self.client_address[0]))
			self.request.settimeout(1200)
			self.request.sendall(b"<Server>: Krampus stares at you. Be nice.\n")
			
			i = 0
			death = 0
	
			while True:
				self.request.sendall(b"<You>: ")
				x= self.request.recv(2048)
				if (i < 2):		
					self.request.sendall(b"<Server>: Krampus approaches.\n")
				elif (i < 4):
					self.request.sendall(b"<Server>: Closer.\n")
				else:
					if (i == 4):
						self.request.sendall(b"<Server>: Krampus is next to you. Act quickly!\n")
					else:
						allgood = True
						
						for r in range (len(x)):
							if (x[r] not in whitelist):
								allgood = False
						
						if (allgood == True):
							bad = 0

							try:
								kid = subprocess.Popen(["python", "krampus.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
								
								wildcard = 0
								while kid.poll() == None:
									if (wildcard == 1):
										x= self.request.recv(2048)

									kid.stdin.write(x)
									wildcard = 1
									time.sleep(1)

								out = kid.stdout.read()
								err = kid.stderr.read()

								if (out != ""):
									self.request.sendall (bytearray('<Krampus>: ' + str(out)[:-1]+ '\n', 'utf8'))
								
								if (err != ""):
									bad = 1
								kid.stdin.close()
								kid.stdout.close()
								kid.stderr.close()
							except Exception as e:
								bad = 1
								print(e.args)

							if (bad == 1):
								self.request.sendall(b"<Server>: Krampus stares back.\n")
						else:
							self.request.sendall(b"<Server>: Krampus grows angry.\n")
							death += 1
							if (death == 5):
								self.request.sendall(b"<e_03>: ???\x07\n")
								break
				i += 1
		except Exception as e:
			self.request.sendall(b"<Server>: Krampus really didn't like that.\n")
			print (e.args)
			pass
	def finish(self):
		pass
				
class ThreadedTCPServer(ss.ThreadingMixIn, ss.TCPServer):
	pass
	
if __name__ == '__main__':
	server = ThreadedTCPServer(('0.0.0.0', 2000), ThreadedTCPRequestHandler)
	server.allow_reuse_address = True
	server.serve_forever()
