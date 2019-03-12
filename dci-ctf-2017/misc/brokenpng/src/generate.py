import sys, struct, random

output = ''

def parse(bytes):
   global output

   signature = bytes[:8]

   output += signature

   bytes = bytes[8:]

   while bytes:
      output += struct.pack('<I', struct.unpack('>I', bytes[:4])[0])
      length = struct.unpack('>I', bytes[:4])[0]
      bytes = bytes[4:]

      print length

      output += bytes[:4].lower()
      chunk_type = bytes[:4]

      bytes = bytes[4:]

      output += bytes[:length]
      chunk_data = bytes[:length]
      bytes = bytes[length:]

      output += struct.pack('<I', random.randint(0, 2**32))

      crc = struct.unpack('>I', bytes[:4])[0]
      bytes = bytes[4:]

      yield chunk_type, crc, chunk_data

def main():
   name = sys.argv[1]

   with open(name, 'rb') as f:
      bytes = f.read()

   for x in parse(bytes):
      pass

   with open('broken.png', 'w') as f:
      f.write(output)

main()
