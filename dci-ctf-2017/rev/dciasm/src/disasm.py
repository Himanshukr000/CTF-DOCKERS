import sys
import struct

program = bytearray(open('auth.bin').read())
ip = 0

while ip < len(program):
    op = program[ip]
    msb = op >> 4

    sys.stdout.write(str(ip) + "\t")

    if op == 0xff:
        print 'syscall'

    elif msb == 1:
        r = (op & 3) + 1

        ip += 1
        d = struct.unpack('H', (program[ip:ip+2]))[0]
        ip += 1

        print 'set r%d, %d' % (r, d)

    elif msb == 2:
        r1 = (op & 3) + 1
        r2 = ((op >> 2) & 3) + 1

        print 'mov r%d, r%d' % (r1, r2)

    elif msb == 3:
        r1 = (op & 3) + 1

        ip += 1
        d = struct.unpack('H', (program[ip:ip+2]))[0]
        ip += 1

        print 'add r%d, %d' % (r1, d)

    elif msb == 4:
        r1 = (op & 3) + 1

        print 'neg r%d' % (r1)

    elif msb == 5:
        r1 = (op & 3) + 1

        ip += 1
        d = struct.unpack('H', (program[ip:ip+2]))[0]
        ip += 1

        print 'mul r%d, %d' % (r1, d)

    elif msb == 6:
        print 'jump r2 if r1 != 0'

    elif msb == 7:
        r1 = (op & 3) + 1
        r2 = ((op >> 2) & 3) + 1

        print 'add r%d, r%d' % (r1, r2)

    else:
        print 'unknown'


    ip += 1
