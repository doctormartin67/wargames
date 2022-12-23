import sys

GROUPS = 1
key = "FREKEY"
letter = 5

"""
if we assume that "E" is the most common letter, then "J" corresponds to "F"
for the first letter of the key. I will continue this process:
J->F
V->R
I->E
O->K
I->E
C->Y

"""

def rotate(s, n):
    return s[n:] + s[:n]

def create_group(s, n):
    group = []
    i = 0
    for a in s:
        if i < letter:
            i += 1
            continue
        if (i - letter) % len(key):
            i += 1
            continue # only looking at first letter of key
        if not i % n:
            group += a
        else:
            group[len(group)-1] += a
        i += 1

    return group

f = open(sys.argv[1])
s = ""
for l in f:
    s += l

s = s.replace(" ", "")

group = []

for i in range(0, GROUPS):
    tmp = rotate(s, i)
    group += create_group(tmp, GROUPS)

count = {i: group.count(i) for i in group}
if 1:
    for key in count.keys():
        print(key, count[key])

if 0:
    print(s)

