import numpy as np
import math

paths = []
for k in range(0,2): #mussichnochgucken
    path = []
    i,j = 6,6
    path.append([i,j])
    while (i,j)>(0,0):
        if i == 0:
            j -=1
            path.append([i,j])
        elif j == 0:
            i-=1
            path.append([i,j])
        else:
            rn= np.random.standard_normal()
            if rn > 0:
                i -= 1
                path.append([i,j])
            else:
                j -= 1
                path.append([i,j])

    if not path in paths:
        paths.append(path)
        #print(path)
    print(len(paths))

result = math.factorial(40)/(math.factorial(20)**2)
print(result)

