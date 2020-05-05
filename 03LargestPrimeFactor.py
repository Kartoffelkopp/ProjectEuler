import multiprocessing as mp


def isprime(zahl):
    output = True
    import math
    for i in range(3, int(math.sqrt(zahl)) + 1, 2):
        if zahl % i == 0:
            output = False
    return output


def checkForTeilerIn10erSchrittenVonBis(startZahl, zahl):
    for i in range(startZahl, zahl, 10):
        if zahl % i == 0:
            print("Checkzahl:", zahl, "Teiler: ", i)
            zahl /= i
            if isprime(i):
                print("Teiler ist prim!")
        print("Rest:", checkzahl)


def kuerzen(zahl):
    iseven = True
    while iseven:
        if zahl % 2 == 0:
            zahl /= 2
        else:
            iseven = False
    return int(zahl)


def primfaktorZerlegung(zahl):
    import math
    primfaktoren = []
    iseven = True
    while iseven:
        if zahl % 2 == 0:
            primfaktoren.append(2)
            zahl /= 2
        else:
            iseven = False

    for i in range(3, int(zahl) + 1, 2):
        while zahl % i == 0 and isprime(i):
            primfaktoren.append(i)
            zahl /= i
    return primfaktoren


checkzahl = 100876

primFaktoren = primfaktorZerlegung(checkzahl)
print(primFaktoren)
