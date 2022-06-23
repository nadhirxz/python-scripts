#USE : caesar_cipher.py [e/d] [filename] [password]
import base64
import sys


def caesar_cipher(m, u, p):
	k = 0
	v = ""
	for i in range(len(p)):
		k += ord(p[i])
		k %= 95
	if m == 0:
		for i in range(len(u)):
			t = ord(u[i])
			if t > 31 and t < 127: t += k - 32
			if t >= 95: t %= 95
			t += 32
			v += chr(t)
	else:
		for i in range(len(u)):
			t = ord(u[i])
			if t > 31 and t < 127: t -= k + 32
			if t < 0: t += 95
			t += 32
			v += chr(t)
	return v


method = sys.argv[1]
name = sys.argv[2]
password = sys.argv[3]
file = open(name, "r")

x = str(file.read())

if method == "e":
	u = base64.b64encode(x.encode('utf-8')).decode('utf-8')
	result = caesar_cipher(0, u, password)
	file = open(name, "w")
	file.write(result)
	print("Encrypted " + name + " successfully !")
else:
	u = caesar_cipher(1, x, password)
	result = base64.b64decode(u.encode('utf-8')).decode('utf-8')
	file = open(name, "w")
	file.write(result)
	print("Decrypted " + name + " successfully !")
