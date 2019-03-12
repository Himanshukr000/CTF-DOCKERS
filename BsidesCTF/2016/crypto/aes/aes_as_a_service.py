import sys
import socket
import random
import hashlib
import Crypto.Cipher.AES as AES
from thread import start_new_thread

class Cipher:
    @staticmethod 
    def md5sum(raw):
        m = hashlib.md5()
        m.update(raw)
        return m.hexdigest()

    def __init__(self):
        random.seed("r4nd0m57r1n6703n5ur3r4nd0m")
        k1 = str(random.random())
        k2 = str(random.random())
        self.cnter_cb_called = 0
        self.secret = self.md5sum(k1)
        self.key = self.md5sum(k2) 

    def enc_counter(self):
        self.cnter_cb_called += 1           
        return self.secret[self.cnter_cb_called % AES.block_size] * AES.block_size
 
    def encrypt(self, raw): 
        c = AES.new(self.key, AES.MODE_CTR, counter = self.enc_counter)
        enc = c.encrypt(raw)
        return enc

    def decrypt(self, enc):
        c = AES.new(self.key, AES.MODE_CTR, counter = self.enc_counter)
        raw = c.decrypt(enc)
        return raw

HOST = '' # all availabe interfaces
PORT = 9999 # arbitrary non privileged port 

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
    conn.send("Welcome to the AEAS (AES Encryption As a Service) server\n")
    conn.send("Please enter the string to be encrypted (max 1024 bytes)\n")
    x = Cipher()
    while True:
        conn.send("Input: ")
        data = conn.recv(1024)
        if not data:
            break
        reply = "Encrypted string: " + x.encrypt(data).encode('hex')  + "\n"
        conn.sendall(reply)
    conn.close()

while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))

    start_new_thread(client_thread, (conn,))

s.close()
