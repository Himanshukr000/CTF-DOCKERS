from os import system, listdir
from random import choice

libs = listdir('libs')
for y in libs:
    x='LD_PRELOAD=libs/{} ./main'.format(y)
    print (x)
