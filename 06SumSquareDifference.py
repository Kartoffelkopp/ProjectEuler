def sumOfSqares(zahl):
    output=0
    for i in range(1,zahl+1):
        output += i*i
    return output

def squareOfSum(zahl):
    sum = 0
    for i in range(1,zahl+1):
        sum += i
    return sum*sum

print(squareOfSum(100)-sumOfSqares(100))