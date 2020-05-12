f = open("Prob13OneHundred50digitNumber.txt","r")

if f.mode == "r":
    content = f.readlines()

zahlen = []
for x in content:
    zahlen.append(int(x))
ergebnis = sum(zahlen)
print(ergebnis)