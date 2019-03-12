#!/usr/bin/python3
# coding=utf-8

import sys,os
import string
import random
import time
import subprocess
from binascii import unhexlify

random.seed(time.time)

charset=string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase

patchbytes=16
print("You are allowed a maximum patch of {} bytes".format(patchbytes))
print("You need to input a patch following format")
print("starting offset[space]ending offset[space]value to be put in hex")
print("Different groups of patches need to be comma separated")
print("Example: 20 21 4141, 65 69 4141424243")

patchstring=input()
patchstring=patchstring.split(',')

numpatch=0
for i in patchstring:
    i=i.split()
    start=int(i[0])
    end=int(i[1])
    patch=unhexlify(i[2])

if end<start:
    print("Invalid input")
    sys.exit(0)    
    
numpatch+=(end-start+1)

if numpatch>patchbytes:
    print("Exceeded patch size")
    sys.exit(0)


f=open('patch','rb')
data=f.read()
f.close()

for i in patchstring:
    i=i.split()
    start=int(i[0])-1
    end=int(i[1])
    try:
        patch=unhexlify(i[2])
    except:
        print("Unsupported Input")
        sys.exit(1)

    temps=data[:start]
    tempe=data[end:]
    data=temps+patch+tempe

filename="/tmp/"

for i in range(10):filename+=charset[random.randint(0,len(charset)-1)]
f=open(filename,'wb')
f.write(data)
f.close()

os.system("chmod +x {}".format(filename))

try:
    process=subprocess.Popen(filename,stdout=subprocess.PIPE)
    response,error = process.communicate()
    print (response.decode('ISO-8859-1'))
except:
    print ("Unable to run patched file")
os.remove(filename)