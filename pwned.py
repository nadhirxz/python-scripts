import requests
import hashlib
import sys

password = input("Your password : ")

hashchars = hashlib.sha1(password.encode()).hexdigest().upper()
x = requests.get("https://api.pwnedpasswords.com/range/"+hashchars[0:5]).text.split("\n")

count = 0
for i in range(len(x)):
    x[i] = x[i].split(":")
    x[i][1] = x[i][1].split("\r")
    if(hashchars[0:5]+x[i][0]==hashchars):
        count = int(x[i][1][0])

if count==0:
    print("No worries mate, your password is safe")
else :
    print(f"Oh that's bad ! You password have appeared on data breaches {str(count)} times")