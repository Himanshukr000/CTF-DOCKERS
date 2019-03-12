#!/usr/bin/env python
import os
from Crypto.Cipher import AES
import SocketServer
import threading
import time


#actual key and iv go here...
key = "00000000000000000000000000000000".decode("hex")
iv  = "00000000000000000000000000000000".decode("hex")

def pkcs(msg):
  print msg.encode("hex")
  padding_length = ord(msg[-1])
  padding = msg[-padding_length:]
  print padding.encode("hex")
  if (padding != (chr(padding_length)*padding_length)):
    print (chr(padding_length)*padding_length).encode("hex")
    return None
  return msg[:-padding_length]

def decrypt(cipher,enc):
  print enc,((len(enc) % 16) != 0)
  dec = ""
  if ((len(enc) % 16) != 0):
    return (False,"Error: cipher length must be a multiple of 16\n")
  dec = cipher.decrypt(enc)
  msg = pkcs(dec)
  if msg is None:
    return (False,"Error: incorrect padding\n")
  return (True,msg)

def process(cmd):
  # Message is like HERE_IS_COMMAND:cmd
  # eg "HERE_IS_COMMAND:help"
  
  cmd = cmd[16:] #ignore the COMMAND: part, it's all the same anyhow
  
  if (cmd == "help"):
    return "Commands:\n\thelp - this\n\tflag - prints out the flag\n\tnyan - prints out a nyan cat\n"
  if (cmd == "flag"):
    return "key: XXX TRY TO READ ME XXX"
  if (cmd == "nyan"):
    return """
+      o     +              o   
    +             o     +       +
o          +
    o  +           +        +
+        o     o       +        o
-_-_-_-_-_-_-_,------,      o 
_-_-_-_-_-_-_-|   /\_/\  
-_-_-_-_-_-_-~|__( ^ .^)  +     +  
_-_-_-_-_-_-_-""  ""      
+      o         o   +       o
    +         +
o        o         o      o     +
    o           +
+      +     o        o      +    
"""
  return "Invalid command. See help for a list of commands\n"

class threadedserver(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class incoming(SocketServer.BaseRequestHandler):
  def handle(self):
    cur_thread = threading.current_thread()
    welcome = """
Enter your encrypted command:
"""
    self.request.send(welcome)
    while True:
      m = self.request.recv(1024)
      cipher = AES.new(key, AES.MODE_CBC, iv)
      success,cmd = decrypt(cipher,m[:-1]) #discard newline
      if (success):
        self.request.send(process(cmd))
      else:
        self.request.send(cmd)

server = threadedserver(("0.0.0.0", 4567), incoming)
server.timeout = 4
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

server_thread.join()
