import os, hashlib, base64

hash_secret = '5Y2g0rt6NbYzmwQF'

def check_sig(signature):
  d = base64.b64decode(signature)
  print "d is {}".format(d)
  # signature:username:0........:1 (sig hex encoded)
  split_vars = d.split(":")
  print "split as {}".format(split_vars)
  print
  # signature, username, 0..., 1
  sig = split_vars[0] # signature
  username = split_vars[1] # username
  role = split_vars[-1] # fake role
  h_string = hash_secret + ''.join(split_vars[1:])  # this needs to be the same as before with modified data
  print "h_string being hashed... {}".format(h_string)
  h = hashlib.sha512(h_string).digest() # 
  en = h.encode('hex')
  print "signature calculated {}".format(en)
  print "signature recieved.. {}".format(sig)
  if sig == en:
    return True
  else:
    return False


def generate_sig(username):
  # Here we need to generate a signature string so that when decoded, appears as
  # [Signature][Data] where [Data] is made up of [Username:Role]
  # id[0] will always be signature, id[1] will always be username (inconsequential), id[-1] will always be role
  # with the hash extension attack, the cookie will become [signature]:[username...................:1] with the same signature as [signature]:[username]:0 
  # SIG = H(SECRET||USERNAME||ROLE)
  # hashsecret|username|:0
  h_string = hash_secret + username + "0"
  print "string being hashed: {}".format(h_string)
  h = hashlib.sha512(h_string).digest()
  en = h.encode('hex')
  return base64.b64encode(en + ":" + username + ":0")


def admin(sig):
    if check_sig(sig):
      if base64.b64decode(sig).split(":")[-1] == "1":
        print "ADMIN!"


username = "peleus"
data = "YWU1ZTE0Y2VlN2M4YzhkMmUzNzQ2MmQ2Y2UwOTI4ZDVjZTcwNmMxYzI4MzAyMzBmMmJlNjZkZjg5NmU5YjFiZDcwODY1ODAyM2FkYmIyM2EzNjkzNjA3OTAyM2UzN2ZmZDBjNjU0MTRhZTUzMDFjZTMyZmJiYWI5ODE2YmQ2MTk6cGVsZXVzMIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuDox"

print "Generating Signature..."
print generate_sig(username)
# Generated - ODliODJmOTJiOTI2ZjdkM2QxYjBjMDkwMzgxZGYwNTEzMGJhOGQ2ZjQ1Y2ZlOTc5Y2M5MjMxOWMyYjU5NzJhNWE3OGRmZmQxYTM4YWMxYzAzODE5ODQ1OWQ2ZmY0NjQ0ZGM0Y2M3YTlkZGI3ZmJhOTI1Y2MyZmJkYTM5NzU4ZDA6cGVsZXVzOjA=

print
print "Checking admin with new hash..."
admin(data)

#./hash_extender --data peleus0 --secret 16 --append 1 --signature 619bfbf54ef4901165d84c7202e1407edb4f6234e63c485c3063e36415a846b88a50dd1eea79badd5830bec6a9547ece0cfc2464650bc0f759e9e0f659144327 --format sha512
#Type: sha512
#Secret length: 16
#New signature: ae5e14cee7c8c8d2e37462d6ce0928d5ce706c1c2830230f2be66df896e9b1bd708658023adbb23a36936079023e37ffd0c65414ae5301ce32fbbab9816bd619
#New string: 70656c657573308000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000b831

# NOTE - Be careful of newline
# NOTE - Hash extender does not have ":" as it's not passed into hashing function, added only in the encoding step. 

# python -c 'import sys; sys.stdout.write("ae5e14cee7c8c8d2e37462d6ce0928d5ce706c1c2830230f2be66df896e9b1bd708658023adbb23a36936079023e37ffd0c65414ae5301ce32fbbab9816bd619:peleus0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb8:1")' | base64
