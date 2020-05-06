start = 900
ende = 999
product = 0
for i in range(start,ende):
    for k in range(start,ende):
        ergebnis = i*k
        reverse = int(str(ergebnis)[::-1])
        if (ergebnis - reverse == 0):
            product = ergebnis
print(product)
