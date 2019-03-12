import socket


class mysocket(object):
    """ My socket class to run for listening """
    
    def __init__(self, host, port, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.host = host
        self.port = port
        self.connect()
    
    def connect(self, host=None, port=None):
        if host is None:
            host = self.host
        if port is None:
            port = self.port
        self.host = host
        self.port = port
        self.sock.connect((host, port))
        
    def sendline(self, msg):
        self.sock.send("".join([str(msg), "\n"]))
    
    def recvline(self):
        line = ""
        cur = ""
        while cur != "\n":
            line = "".join([line, cur])
            cur = self.sock.recv(1)
        return line
    
    def close(self):
        self.sock.close()
