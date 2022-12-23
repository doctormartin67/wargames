import sys

key = "FREKEY"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
assert(len(alpha) == 26)

f = open(sys.argv[1])
s = ""

for l in f:
    s += l

s = s.replace(" ", "")

i = 0
for a in s:
    print(alpha[(alpha.find(a) - alpha.find(key[i])) % 26], end="")

    i += 1
    i %= len(key)

print()

