import random, base64

# used this as reference : https://gist.github.com/JonCooperWorks/5314103


# copied
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a


# Euclid's extended algorithm for finding the multiplicative inverse of two numbers
# copied (thanks stackoverflow)
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)


def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m


# copied
def is_prime(num):
	if num == 2:
		return True
	if num < 2 or num % 2 == 0:
		return False
	for n in range(3, int(num**0.5) + 2, 2):
		if num % n == 0:
			return False
	return True


def generate(p, q):
	# enable this if you want the user to input the two primes
	#if p == q: print("p and q cannot be equal !")
	# elif not (is_prime(p) and is_prime(q)): print("p and q must be prime numbers")
	#else :
	n = p * q
	phi = (p - 1) * (q - 1)
	e = random.randint(1, phi)
	g = gcd(e, phi)
	print(f"phi = {phi}")
	while g != 1:
		e = random.randint(1, phi)
		g = gcd(e, phi)
	d = modinv(e, phi)
	return ((e, n), (d, n))


def encrypt(text, key):
	e, n = key
	cipher = [(ord(i)**e) % n for i in text]
	return cipher


def decrypt(cipher, key):
	d, n = key
	text = [chr((i**d) % n) for i in cipher]
	return "".join(text)


def generate_primes(n):  # this is a sieve
	numbers = [True for i in range(n + 1)]
	current = 2
	while (current * current <= n):
		if numbers[current]:
			for i in range(current * current, n + 1, current):
				numbers[i] = False
		current += 1
	return [i for i in range(2, n) if numbers[i]]


def prime_pair(n):  # Goldbach's conjecture (Every even integer greater than 2 can be expressed as the sum of two primes)
	numbers = generate_primes(n)
	i = 0  # i = len(numbers)//2 (if you want to start from the middle)
	while (numbers[i] <= n // 2):  # while (i>1):
		difference = n - numbers[i]
		if (difference in numbers):
			return (numbers[i], difference)
		i += 1


"""
primes = generate_primes(200)
p, q = random.choice(primes), random.choice(primes)
while p == q:
    q = random.choice(primes)
"""
text = input("Your text : ")
password = input("Your password : ")
k = sum([ord(i) for i in password])

if (k % 2 != 0): k += 1
print(f"key = {k}")

p, q = prime_pair(k)
public_key, private_key = generate(p, q)
cipher = encrypt(text, public_key)
cipher_txt = base64.b64encode((":".join(str(i) for i in cipher)).encode("ascii")).decode("ascii")
c = base64.b64decode(cipher_txt.encode("ascii")).decode("ascii")
ciphers = map(int, c.split(":"))
txt = decrypt(ciphers, private_key)

pbk = str(public_key[0]) + ":" + str(public_key[1])
pubk = base64.b64encode(pbk.encode("ascii")).decode("ascii")
prk = str(private_key[0]) + ":" + str(private_key[1])
prik = base64.b64encode(prk.encode("ascii")).decode("ascii")

print(f"p = {p} , q = {q}")
print(f"Strings : Public key = {pubk} , Private key = {prik}")
print(f"Public key = {public_key} , Private key = {private_key}")
print(f"Cipher = {cipher}")
print(f"Cipher text = {cipher_txt}")
print(f"Text = {txt}")