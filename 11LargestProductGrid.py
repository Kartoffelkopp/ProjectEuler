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

product=0
matrixGrid = np.array(grid)
#left-right
# for i in range(0,17):
#     p = matrixGrid[:,i:i+4]
#     for zeile in p:
#         zeilenprod = math.prod(zeile)
#         print(zeilenprod)

test = np.array([[1,2,3],[2,3,4]])
