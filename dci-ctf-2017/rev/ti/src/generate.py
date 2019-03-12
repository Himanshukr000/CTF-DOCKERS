import numpy as np
import random
import os

password = np.array(bytearray('s0lve_s4uve_d3s_v1es'), dtype=int)
n = len(password)
system = np.zeros((n, n + 1), dtype=int)

for i in range(n):
    s = 0
    for j in range(n):
        x = random.randint(5, 50)
        system[i][j] = x
        s += password[j] * x

    system[i][-1] = s


print system

code = '''
volatile unsigned int v[N] = {0};
volatile unsigned int state = 0;

int main(int argc, char **argv) {
  if(argc != 2) {
    printf("usage: %s [password]\\n", argv[0]);
    return 1;
  }

  char *k = argv[1];

CODE

  for(int i = 0; i < 9; i++) {
    if(v[i] != 0) {
      puts("Invalid password");

      return 0;
    }
  }

  printf("DCI{%s}\\n", argv[1]);
}
'''.replace('N', str(n))

instructions = []

for i in range(n):
    instructions.append(((i,j), '  v[%d] -= %d;' % (i, system[i][-1])))

    for j in range(n):
        instructions.append(((i, j), '  v[%d] += k[%d] * state;' % (i, j)))


random.shuffle(instructions)

output = []
state = 0

for ((i, j), inst) in instructions:
    x = system[i][j]
    diff = x - state
    state += diff

    assert state == x

    output.append('  state += %d;' % diff)
    output.append(inst)

code = code.replace('CODE', '\n'.join(output))

with open('ti.c', 'w') as f:
    f.write(code)

os.system("gcc -O3 ti.c -o ti")
os.system("strip ti")
