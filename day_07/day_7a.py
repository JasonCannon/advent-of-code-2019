from itertools import permutations
import subprocess

mx = 0
for l in permutations(range(0, 5)):
    inp = '0'
    for p in l:
        process = subprocess.run('python3 day_7a_intcode.py', shell=True, universal_newlines=True, input="{}\n{}".format(p, inp), stdout=subprocess.PIPE)
        inp = process.stdout.strip()
    mx = max(mx, int(inp))
print(mx)
