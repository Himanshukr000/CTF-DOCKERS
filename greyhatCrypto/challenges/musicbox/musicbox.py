import sys, struct, array
import SocketServer
# import StringIO as StringIO
# import pygame

p = 0x08d682598db70a889ff1bc7e3e00d602e9fe9e812162d4e3d06954b2ff554a4a21d5f0aab3eae5c49ac1aec7117709cba1b88b79ae9805d28ddb99be07ba05ea219654afe0c8dddac7e73165f3dcd851a3c8a3b6515766321420aff177eaaa7b3da39682d7e773aa863a729706d52e83a1d0e34d69b461c837ed239745d6c50f124e34f4d1d00ad15d6ebabda8c189c7b8b35b5bae7a9cbafc5f09bd506a39bd9d2d9245324f02ff7254fab4ab17f7a165d49e318baeb8effc4e1a3f1251d2ea1ab93f767bd6dcf5567406550ea1f194ef7deb1b2fec8b30520b6777fea1b305593db941f9ad8ce1eba6f77c3a104bd97448ec0c11688c5bf82e85c90234abfc5
q = 0x0f67e886d1a0d1e59a53b4aa831c9bcb39a5d0a8f
g = 0x27d6a1359821e2a758a93f5c06ebb26382a06a4681e7cf44d71aeff2390c87d20ce7cd885fb01fd84ad9d52839a8ae163bfee5d09820fea1a09f814801cb157b2c5bc4636d042fb2ac1a836f33adafd6735826ae1e96c3bfbd04f7df672a14120f6780e8848ff3b3123004654127c9d25843cd54c68c396a410a2f0496e8ebb35b971993dee0f596388911277fce46ff3c5191e7e76262875bb3368724d3a40c852ccc80be4dc82335fb9267c6ff0e20396ae8bb2d51e35f15fbd07fa1b354944c285367ac88763dd00fe6fe0aab5a49faf7bc10f8e90ba376efdc034e9e1cae7e79ac906aed3b513c5f3452dc33eb307ab3d45efe92a31b1cd9a6f52dd5fb09
y = 0x6bff47f5ea736b03c85885b0bd0f1f7fa2a7efef8812c544ab47f4aa3542235f5a298fc778bb9263223c66d149f88d377b1e70a5715e4554776127ffb874e218d7c75a3c6202cc3e2cfb6a5a4cf34e7e8d5428b90b7aa1dbf9a7e965feab029220266ad0dabade6ae09362f6463eea60e3133bb79fc4af511057e31574f4b0f34b848b180fa20da7d9a6d8adedded9819da20b8923073e35f43ca75eeb9a1ab5451c3a5446306f93ef246759f59e65e498032d48aece56f437b4b7179daf3dfa80d6a36c211ed5acdfeaf91a7e8070a49a521f3c2e411a26eeaf8fab697535914982f1f7cda1e1aa1aac602f9606ea326632b4fbabf6b361fe118637e048c482

def bytesToInt(s):
	x = 0
	for c in s:
		x = (x << 8) | ord(c)
	return x

def verifySig(r, s, m):
	#DSA, straight from Wikipedia
	if not 0 < s < q and 0 < r < q:
		return False
	w = pow(s, q-2, q)
	u1 = m*w % q
	u2 = r*w % q
	v = pow(g, u1, p) * pow(y, u2, p) % p
	return (v % q) == r

def superHash(b):
	b += '0' * (-len(b) % 2)

	h = (len(b) + 1) * (len(b) ^ 42)
	x = 88172645463325252
	for i, c in enumerate(array.array('H', b)):
		x ^= (x<<13) & 0xFFFFFFFFFFFFFFFF
		x ^= (x>>7)  & 0xFFFFFFFFFFFFFFFF
		x ^= (x<<17) & 0xFFFFFFFFFFFFFFFF

		h += c * (((i % 7) + 9) ** (i % 25))
		if i % 2:
			h *= x | i
		else:
			h += x | i
		h &= 0xFFFFFFFFFFFFFFFF

	h ^= (len(b) ^ 1) * (len(b) + 42)
	h &= 0xFFFFFFFFFFFFFFFF
	return h

class HandleCheckin(SocketServer.BaseRequestHandler):
	def readStr(self):
		req = self.request
		prefix = req.recv(2)
		if prefix != '\x12\xae':
			req.sendall("Incorrect prefix\n")
			req.close()
			return None

		leng = struct.unpack("<I", req.recv(4))[0]
		toRead = ""
		while len(toRead) < leng:
			toRead += req.recv(leng - len(toRead))
		if len(toRead) > leng:
			req.sendall("Length does not match input data size\n")
			req.close()
			return None
		return toRead

	def handle(self):
		req = self.request
		req.sendall("""Welcome to the new and improved Music Box! Please provide your signed music file.""")

		data = self.readStr()
		if data is None or len(data) < 48:
			req.sendall("Incomplete header\n")
			return
		elif len(data) > 12345678:
			req.sendall("The data. It is too much!\n")
			return

		r = bytesToInt(data[:20])
		s = bytesToInt(data[20:40])
		h = bytesToInt(data[40:48])
		sound = data[48:]

		if not verifySig(r, s, h):
			req.sendall("Invalid signature\n")
			return
		elif h != superHash(sound):
			req.sendall("Message hash does not match\n")
			return
		else:
			req.sendall("Success!\n")

			if "Secret backdoor lol GIMME THE FLAG" in sound:
				with open('flag.txt','r') as f:
					req.sendall(f.read() + "\n")
			else:
				req.sendall("Unfortunately, the musicbox is not available at the moment.\n")
			req.close()

		# f = StringIO.StringIO(sound)
		# pygame.mixer.music.load(f)
		# pygame.mixer.music.play(loops=-1)

class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ ==  "__main__":
	# pygame.mixer.init()

	HOST, PORT = sys.argv[1], int(sys.argv[2])
	print 'Running on port', PORT
	server = ThreadedServer((HOST, PORT), HandleCheckin)
	server.allow_reuse_address = True
	server.serve_forever()
