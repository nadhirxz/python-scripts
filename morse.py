import winsound
import time
import sys

frequency = 2500
dot = 300
dash = dot * 3
lspace = dot * 3
wspace = dot * 7

morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ', ': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-'
}
while True:
	u = input("Enter text : ")
	execute = True
	for i in range(len(u)):
		key = u[i].upper()
		if key not in morse and key != " ":
			print(key + " character cannot be translated to morse code.")
			execute = False
			break
	if execute:
		print("Output : ", end="")
		for i in range(len(u)):
			print(u[i], end="")
			sys.stdout.flush()
			if u[i] == " ":
				time.sleep(wspace / 1000)
			else:
				v = morse[u[i].upper()]
				for k in range(len(v)):
					winsound.Beep(frequency, dot) if v[k] == "." else winsound.Beep(frequency, dash)
				time.sleep(lspace / 1000)
		print()
