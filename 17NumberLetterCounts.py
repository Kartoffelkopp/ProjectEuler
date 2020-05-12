# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


zahlen = {
    0 : "",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

laenge = []
wortzahlen =[]

for i in range(1,21):
    laenge.append(len(zahlen[i]))
    wortzahlen.append(zahlen[i])

for i in range(21,1000):
    zahl = str(i)
    if len(zahl)==2:
        wortzahl = zahlen[int(zahl[0])*10]+zahlen[int(zahl[1])]
    else:
        if zahl[1:] == "00":
            wortzahl = zahlen[int(zahl[0])] + "hundred"
        elif int(zahl[1:]) in range(1,20):
            wortzahl = zahlen[int(zahl[0])] + "hundredand"+zahlen[int(zahl[1:])]
        else:
            wortzahl = zahlen[int(zahl[0])]+"hundredand"+zahlen[int(zahl[1])*10]+zahlen[int(zahl[2])]
    wortzahlen.append(wortzahl)
    laenge.append(len(wortzahl))


thousand = "onethousand"
wortzahlen.append(thousand)
laenge.append(len(thousand))
print(list(zip(wortzahlen,laenge)))

ergebnis = sum(laenge)
print(ergebnis)



