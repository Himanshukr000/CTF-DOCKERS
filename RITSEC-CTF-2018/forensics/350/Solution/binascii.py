import sys
def decode_binary_string(s):
	return(''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8)))
print(decode_binary_string(sys.argv[1]))
