#USE : b64.py [e/d] [filename]
import base64
import sys

method = sys.argv[1]
name = sys.argv[2]
file = open(name,"r")
x = str(file.read())

if method == "e":
    result = base64.b64encode(x.encode('utf-8')).decode('utf-8')
    file = open(name,"w")
    file.write(result)
    print("Encoded " + name + " successfully !")
else:
    result = base64.b64decode(x.encode('utf-8')).decode('utf-8')
    file = open(name,"w")
    file.write(result)
    print("Decoded " + name + " successfully !")