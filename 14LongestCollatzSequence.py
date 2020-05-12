def CollatzSequenz(n):
    sequenz = [n]
    while n>1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
        sequenz.append(n)
    return sequenz


def CollatzSequenzLength(n):
    iterator = 1
    while n>1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
        iterator +=1
    return iterator


N=1000000
length = 1
zahl = 1
import time
start = time.process_time()
for i in range(1,N):
    if CollatzSequenzLength(i) > length:
        length = CollatzSequenzLength(i)
        zahl = i


print(zahl,length, (time.process_time()-start))