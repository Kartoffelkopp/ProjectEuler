def AnzahlTeilers(n):
    anzahl = 0
    c = int(n**.5)+1
    for i in range(1,c):
        if n%i==0:
            anzahl +=2
    return anzahl

for i in range(1,10**100):
    if (AnzahlTeilers(.5*i*(i+1)))>500:
        print("T={0}".format(.5*i*(i+1)))
        break



