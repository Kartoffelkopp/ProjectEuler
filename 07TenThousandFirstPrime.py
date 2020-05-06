def isprime(zahl):
    output = True
    i=3
    while i*i<= zahl:
        if zahl % i == 0:
            output = False
            break
        else:
            i+=2
    return output

primenumbers =[2,3]

i=5
while len(primenumbers) <=10000:
    if isprime(i):
        primenumbers.append(i)
    i +=2

print(primenumbers[10000])
