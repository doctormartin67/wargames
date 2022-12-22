import sys

GROUPS = 4

def rotate(s, n):
    return s[n:] + s[:n]

def create_group(s, n):
    group = []
    i = 0
    for a in s:
        if not i % n:
            group += a
        else:
            group[len(group)-1] += a
        i += 1

    count = {i: group.count(i) for i in group}
    return group

f = open(sys.argv[1])
s = ""
for l in f:
    s += l

s = s.replace(" ", "")

s = s.replace("J", "t")
s = s.replace("D", "h")
s = s.replace("S", "e")

s = s.replace("Q", "a")
#s = s.replace("F", "v")

s = s.replace("G", "n")
s = s.replace("W", "d")

s = s.replace("C", "i")
s = s.replace("T", "m")

s = s.replace("U", "s")
s = s.replace("A", "b")
s = s.replace("X", "f")
s = s.replace("O", "x")

"""
used krypton4 for the following replaces guesses:
"""

s = s.replace("Y", "p")
s = s.replace("K", "w")
s = s.replace("B", "o")
s = s.replace("N", "r")
s = s.replace("V", "l")
s = s.replace("M", "u")

print(s)
sys.exit(0)

group = []

for i in range(0, GROUPS):
    tmp = rotate(s, i)
    group += create_group(tmp, GROUPS)
count = {i: group.count(i) for i in group}
for key in count.keys():
    print(key, count[key])

