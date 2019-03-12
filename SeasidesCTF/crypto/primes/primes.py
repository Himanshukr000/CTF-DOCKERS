import random
import binascii

def Random_String_Generator(length):   
    msg = "" 
    
    while len(msg)!=length:
        i = random.randint(1,255)
        j = random.randint(1,255)
        
        s = (i*j)%128
        
        if s<33:
            s = random.randint(33,128)
        
        msg += str(chr(s))

    return(msg)
    
def xor(m,k):
    key = str(k)
    
    ct = ""
    j = 0
    for i in range(len(m)):
        ct += chr(ord(key[i%(len(key))])^ord(m[i]))
    return(binascii.hexlify(ct.encode()))

FLAG = "sea{L00K_CL053LY}sides"

cnt = random.randint(40,60)
f = random.randint(20,30)

for i in range(cnt):
    alpha = random.randint(800000000,1000000000)
    p = random.randint(350000000000000,5500000000000000)
    print("\n\nAplha:",alpha)
    print("P:",p)
    
    A = int(input("\nGive me your A: "))
    b = random.randint(1,10)
    B = pow(alpha,b,p)
    print("Take my B:",B)
    
    KEY = pow(A,b,p)
    
    if i==f:
        m = FLAG
        ct = xor(m,KEY)
        
    else:
        l = random.randint(20,30)
        m = Random_String_Generator(l)
        ct = xor(m,KEY)
        
    print("\nCiphertext:",ct)
    
    pt = input("\nPlaintext(encoded in hex): ")
    
    if binascii.unhexlify(pt).decode() == m:
        continue
    else:
        print("\n oof, try again")
        break

print("\nThanks for playing :)")