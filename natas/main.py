import sys
import requests as req
import hashlib

username = "natas33"
password = "APwWDD3fRAf6226sgBOBaSptGwvXwQhG"
url = "http://%s.natas.labs.overthewire.org/" % username

s = req.session()

def get(s):
	r = s.get(url, auth=(username, password))
	return r

def post(s, data):
	r = s.post(url, auth=(username, password), data=data)
	return r

def upload(s, files, data=None):
	if not data:
		r = s.post(url, auth=(username, password), files=files)
		return r
	r = s.post(url, auth=(username, password), files=files, data=data)
	return r

if __name__ == "__main__":
	filename = "test.php"
	data = {"filename": filename}
	files = {"uploadedfile": open(filename, "rb")}
	r = upload(s, files=files, data=data)
	#r = get(s)
	print(r.text)
	print(r.request.body)

	file_contents = "adeafbadbabec0dedabada55ba55d00d"
	result = hashlib.md5(bytes(file_contents, "utf-8")).hexdigest()
	print(result)
