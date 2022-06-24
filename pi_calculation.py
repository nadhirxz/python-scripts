import time,sys,math
from decimal import Decimal,localcontext
pi = 3
i = 0
with localcontext() as ctx:
    try:
        ctx.prec = sys.argv[1]
    except :
        ctx.prec = 100
    try:
        while True :
            add = 4*Decimal(((-1)**i)/Decimal(Decimal(Decimal(2*i+3)**3)-Decimal(2*i+3)))
            pi += add
            i+=1
            print(pi,end="\r")
            time.sleep((i**2)/(i**3))
            print('\b'*len(str(pi)),end="",flush=True)
    except KeyboardInterrupt:
        print("\nDone")