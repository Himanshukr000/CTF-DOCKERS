import sys
import socket
from thread import start_new_thread

HOST = '' # all availabe interfaces
PORT = 10003 # arbitrary non privileged port

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
    sys.exit(0)

print("[-] Socket Created")

# bind socket
try:
    s.bind((HOST, PORT))
    print("[-] Socket Bound to port " + str(PORT))
except socket.error, msg:
    print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
    sys.exit()

s.listen(10)
print("Listening...")

def client_thread(conn):
	conn.send("Please send through the number\n")
	g = int(conn.recv(1024))
	conn.send("Checking 1 mod 3 requirement...")
	if g % 3 == 1:
		conn.send("PASS\n")
		conn.send("Checking 1 mod 19 requirement...")
		if g % 19 == 1:
			conn.send("PASS\n")
			conn.send("Checking 1 mod 5 requirement...")
			if g % 5 == 1:
				conn.send("PASS\n")
				conn.send("Checking 7 mod 23 requirement...")
				if g % 23 == 7:
					conn.send("PASS\n")
					conn.send("Checking 8 mod 11 requirement...")
					if g % 11 == 8:
						conn.send("PASS\n")
						conn.send("Checking 10 mod 13 requirement...")
						if g % 13 == 10:
							conn.send("PASS\n")
							conn.send("Checking 1 mod 2 requirement...")
							if g % 2 == 1:
								conn.send("PASS\n")
								conn.send("Checking 6 mod 17 requirement...")
								if g % 17 == 6:
									conn.send("PASS\n")
									conn.send("Checking 5 mod 7 requirement...")
									if g % 7 == 5:
										conn.send("PASS\n")
										conn.send("Checking 12 mod 29 requirement...")
										if g % 29 == 12:
											conn.send("PASS\n")
											conn.send("BSIDES_CTF{252291eb275d703a1eeceba9e27fae60}\n")
											return
	conn.send("FAIL")
	return

while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))

    start_new_thread(client_thread, (conn,))

s.close()
