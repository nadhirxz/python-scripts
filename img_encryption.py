from PIL import Image
import hashlib, argparse


def caesar_cipher(m, u, p):
	k = 0
	v = []
	for i in range(len(p)):
		k += ord(p[i])
		k %= 256
		if k == 0: k = 23
	for i in range(len(u)):
		if m == 0: v.append((u[i] + k) % 256)
		else: v.append((u[i] - k) % 256)
	return v


def vigenere_cipher(m, u, key):
	v = []
	for i in range(len(u)):
		if m == 0: v.append((u[i] + ord(key[i % len(key)])) % 256)
		else: v.append((u[i] - ord(key[i % len(key)])) % 256)
	return v


def xor_cipher(m, u, p):
	for i in range(len(u)):
		u[i] = u[i] ^ ord(p[i % len(p)])
	return u


def cipher(m, a, password):
	#p = str(hashlib.sha512(password[:int(len(password)/2)].encode()).hexdigest())+str(hashlib.sha512(password[int(len(password)/2):-1].encode()).hexdigest())
	p = []
	p.append(str(hashlib.md5(password.encode()).hexdigest()))
	p.append(str(hashlib.sha256(password.encode()).hexdigest()))
	p.append(str(hashlib.sha3_256(password.encode()).hexdigest()))
	p.append(str(hashlib.sha3_512(password.encode()).hexdigest()))
	p.append(str(hashlib.blake2s(password.encode()).hexdigest()))
	p.append(str(hashlib.shake_256(password.encode()).hexdigest(256)))

	functions = [xor_cipher, caesar_cipher, vigenere_cipher, xor_cipher, vigenere_cipher, caesar_cipher]
	passwords = [p[0], p[1], p[2], p[3], p[4], p[5]]
	if m == 0:
		for i in range(len(functions)):
			a = functions[i](0, a, passwords[i])
		"""
        a = xor_cipher(a,p[0])
        a = caesar_cipher(0,a,p[1])
        a = vigenere_cipher(0,a,p[2])
        a = xor_cipher(a,p[0])
        a = vigenere_cipher(0,a,p[2])
        a = vigenere_cipher(0,a,p[2])
        a = caesar_cipher(0,a,p[1])
        a = xor_cipher(a,p[0])
        a = caesar_cipher(0,a,p[1])"""
	else:
		for i in range(len(functions) - 1, -1, -1):
			a = functions[i](1, a, passwords[i])
		"""
        a = caesar_cipher(1,a,p[1])
        a = xor_cipher(a,p[0])
        a = caesar_cipher(1,a,p[1])
        a = vigenere_cipher(1,a,p[2])
        a = vigenere_cipher(1,a,p[2])
        a = xor_cipher(a,p[0])
        a = vigenere_cipher(1,a,p[2])
        a = caesar_cipher(1,a,p[1])
        a = xor_cipher(a,p[0])"""
	return a


def encrypt(image, password):
	pixels = img.load()
	W, H = img.size
	password = str(hashlib.sha512(password.encode()).hexdigest())
	a = []
	for i in range(W):
		for j in range(H):
			for u in range(3):
				a.append(pixels[i, j][u])

	a = cipher(0, a, password)

	k = 0
	for i in range(W):
		for j in range(H):
			pixels[i, j] = (a[k], a[k + 1], a[k + 2])
			k += 3
	return img


def decrypt(img, password):
	pixels = img.load()
	W, H = img.size
	password = str(hashlib.sha512(password.encode()).hexdigest())
	p = str(hashlib.sha512(password[:int(len(password) / 2)].encode()).hexdigest()) + str(str(hashlib.sha512(password[int(len(password) / 2):-1].encode()).hexdigest()))

	a = []
	for i in range(W):
		for j in range(H):
			for u in range(3):
				a.append(pixels[i, j][u])

	a = cipher(1, a, password)

	k = 0
	for i in range(W):
		for j in range(H):
			pixels[i, j] = (a[k], a[k + 1], a[k + 2])
			k += 3
	return img


ap = argparse.ArgumentParser()
group = ap.add_mutually_exclusive_group(required=True)
group.add_argument("-e", action="store_true", help="Encrypt")
group.add_argument("-d", action="store_true", help="Decrypt")
ap.add_argument("-i", "--image", required=True, help="Input image")
ap.add_argument("-o", "--output", required=False, help="Output image")
ap.add_argument("-p", "--password", required=True, help="Your password")
args = vars(ap.parse_args())

image = args["image"]
password = args["password"]
if args["output"]: output = args["output"]
else: output = "output." + image.split(".")[-1]
img = Image.open(image)

if args["e"]:
	im = encrypt(img, password)
	im = decrypt(im, password[len(password) - 1:])
	im.save(output)
	print(image + " encrypted successfully !")
else:
	im = encrypt(img, password[len(password) - 1:])
	im = decrypt(im, password)
	im.save(output)
	print(image + " decrypted successfully !")
