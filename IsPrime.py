def isprime(zahl):
    output = True
    if isinstance(zahl, int):
        if zahl <2:
            output = False
            print("Zahl ist zu klein")
        elif zahl == 2 or zahl == 3:
            return output
        else:
            import math
            for i in range(2, math.floor(math.sqrt(zahl))+1):
                if zahl % i == 0:
                    output = False
                    break
    else:
        output = False
        print("Zahl ist keine positive ganze Zahl")
    return output