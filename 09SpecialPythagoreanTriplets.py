
import time
start = time.process_time_ns()
a=1
while a<1000:
    b=(500000 - 1000*a)/(1000-a)
    if b.is_integer():
        c = 1000 - a - b
        break
    a +=1
print("a=", a," b=",b," c=",c," abc=", a*b*c)
print("Runtime: ",  time.process_time_ns()- start)