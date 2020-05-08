import numpy as np
import math
f = open("20x20Grid.txt","r")
if f.mode == "r":
    content = f.readlines()

grid = []

for x in content:
    x = "".join(x.split())
    zeile = []
    for i in range(0,len(x),2):
        zeile.append(int(x[i])*10 + int(x[i+1]))
    grid.append(zeile)

matrixGrid = np.array(grid)
product=0
#left-right
for j in range(0,17):#spalten
    for i in range(0,20):#zeilen
        p = math.prod(matrixGrid[i,j:j+4])
        if p>product:
            product=p

#oben-unten
for j in range(0,20):#spalten
    for i in range(0,17):#zeilen
        p = math.prod(matrixGrid[i:i+4,j])
        if p>product:
            product=p

#diagonal
for j in range(0,17):#spalten
    for i in range(0,17):#zeilen
        p = matrixGrid[i,j]*matrixGrid[i+1,j+1]*matrixGrid[i+2,j+2]*matrixGrid[i+3,j+3]
        if p>product:
            product=p

#antidiagonal
for j in range(0,17):#spalten
    for i in range(0,17):#zeilen
        p = matrixGrid[i,j+3]*matrixGrid[i+1,j+2]*matrixGrid[i+2,j+1]*matrixGrid[i+3,j]
        if p>product:
            product=p

print(product)
