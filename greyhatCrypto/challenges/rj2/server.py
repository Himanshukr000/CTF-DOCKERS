import socket
import sys

from rj2 import enc

key = "487d42bd96333b67".decode('hex')

if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    while True:
        data, addr = sock.recvfrom(1024)
        data = data[:len(data) - len(data) % 8]

        print data

        output = []
        for i in xrange(0, len(data), 8):
            output.append(enc(data[i:i+8], key))
        sock.sendto(''.join(output), addr)
