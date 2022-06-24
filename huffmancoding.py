import heapq

def makeTree(f):
	heap = []
	for a in f:
		heapq.heappush(heap, [a])
	while (len(heap) > 1):
		left = heapq.heappop(heap)
		right = heapq.heappop(heap)
		lfreq, la = left[0]
		rfreq, ra = right[0]
		frequency = lfreq + rfreq
		a = "".join(sorted(la + ra))
		node = [(frequency, a), left, right]
		heapq.heappush(heap, node)
	return heap.pop()


def makeCodes(tree, themap, prefix):
	if (len(tree) == 1):
		f, v = tree[0]
		themap[v] = prefix
	else:
		v, left, right = tree
		makeCodes(left, themap, prefix + "0")
		makeCodes(right, themap, prefix + "1")


def encode(text):
	freq = dict()
	for a in text:
		if a in freq: freq[a] += 1
		else: freq[a] = 1
	freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}

	for a in freq.keys():
		frequencies.append((freq[a], a))
	tree = makeTree(frequencies)
	makeCodes(tree, codes, '')

	output = ""
	for a in text:
		output += codes[a]
	return output


def decode(text):
	output = ""
	tree = thewholetree = makeTree(frequencies)
	for a in text:
		if (a == "0"): tree = tree[1]  # left child
		else: tree = tree[2]  # right child
		if (len(tree) == 1):
			f, v = tree[0]
			output += v
			tree = thewholetree
	return output


def bitstring_to_bytes(s):
	v = int(s, 2)
	b = bytearray()
	while v:
		b.append(v & 0xff)
		v >>= 8
	return bytes(b[::-1])


frequencies = []
codes = dict()
x = open("text.txt", "r").read()
x = encode(x)
nbytes = int(len(x) / 7)
print(nbytes)
s = int(x[::-1], 2).to_bytes(nbytes, 'little')

open("encoded.huf", "wb").write(s)

s = open("encoded.huf", "rb").read()
s = "{:08b}".format(int(s.hex(), 16))

x = decode(s)
print(x)

# doesn't work quite well
# maybe i'll fix it someday