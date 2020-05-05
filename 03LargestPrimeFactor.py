def isprime(zahl):
    output = True
    import math
    for i in range(3, int(math.sqrt(zahl)) + 1, 2):
        if zahl % i == 0:
            output = False
    return output


primefactors = [0]

checkzahl = 600851475143

for i in range(3, int(checkzahl), 2):
    if checkzahl % i == 0:
        print("Checkzahl:", checkzahl,"Teiler: ", i)
        if isprime(i):
            print("Teiler ist prim!")
        checkzahl = checkzahl/i
        print("Rest:", checkzahl)

print(primefactors)
