def sieb_des_Erathostenes(n):
    import numpy as np
    import math
    flags = np.ones(n, dtype=bool)
    flags[0] = flags[1] = False

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if flags[i]:
            flags[i*i::i]=False

    return np.flatnonzero(flags)
