def isprimeWhile(zahl):
    output = True
    i=3
    while i*i<= zahl:
        if zahl % i == 0:
            output = False
            break
        i+=2
    return output

def isprimeFor(zahl):
    output = True
    import math
    wurzel = int(math.sqrt(zahl))+1
    for i in range(3,wurzel,2):
        if zahl % i == 0:
            output = False
            break
    return output

import time
start = time.process_time()
ergebnis=5

for i in range(5,2000000,2):
    if isprimeFor(i):
        ergebnis += i

print(ergebnis,"\n Process Time: %s s" %(time.process_time() - start))
