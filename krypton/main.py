import sys

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
assert(len(alpha) == 26)

def rotate(s, n):
    return s[n:] + s[:n]

def create_group(s, key_len, letter):
    group = []
    i = 0
    for a in s:
        if i < letter:
            i += 1
            continue
        if (i - letter) % key_len:
            i += 1
            continue # only looking at first letter of key
        group += a
        i += 1

    return group

def decrypt(file_name, key):
    f = open(file_name)
    s = ""
    for l in f:
        s += l

    s = s.replace(" ", "")
    i = 0
    for a in s:
        print(alpha[(alpha.find(a) - alpha.find(key[i])) % 26], end="")

        i += 1
        i %= len(key)

def letters(file_name, key_len, letter):
    f = open(file_name)
    s = ""
    for l in f:
        s += l

    s = s.replace(" ", "")
    group = create_group(s, key_len, letter)
    count = {i: group.count(i) for i in group}
    return count

def addtod(d1, d2):
    for k in d1.keys():
        if k in d2.keys():
            d1[k] += d2[k]

    for k in d2.keys():
        if k not in d1.keys():
            d1[k] = d2[k]

if __name__ == "__main__":
    key_len = int(sys.argv[1])

    key = ""
    for i in range(0, key_len):
        l1 = letters("found1", key_len, i)
        l2 = letters("found2", key_len, i)
        l3 = letters("found3", key_len, i)

        d = {}
        addtod(d, l1)
        addtod(d, l2)
        addtod(d, l3)

        key += alpha[(ord(max(d, key=d.get)) - ord("E")) % 26]

    print(key)
    decrypt("krypton6", key)

