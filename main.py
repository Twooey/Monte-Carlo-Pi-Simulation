import math
import random
import progressbar
import numba

@numba.jit(nopython=True, parallel=True)
def randomPi(throws):
    inCircle = 0
    for i in numba.prange(throws):

        if math.hypot(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)) <= 1:
            inCircle += 1
    pi = (4.0 * inCircle) / throws
    return pi


pi = randomPi(1000000000000)
print(pi)
