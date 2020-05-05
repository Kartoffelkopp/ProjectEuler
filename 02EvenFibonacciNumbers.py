ergebnis = 2
alt = 1
neu = 2
fib = alt + neu

while fib <= 4000000:
    if fib % 2 == 0:
        ergebnis += fib
    alt = neu
    neu = fib
    fib = alt + neu
print(ergebnis)


