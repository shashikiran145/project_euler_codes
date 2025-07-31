# This problem is related to multi set permutations. Also, it can be formulated as a
# combinations nCr problem. I should have figured out that no matter how many ways are there,
# there will always be m+n steps, m and n being the number of grids horizontally and vertically.
# So the problem becomes (m+n)Cm. So, for 20x20 grid, it will be 40C20

import math


def combination(m, n):
    return (math.factorial(m+n))/(math.factorial(m)*math.factorial(n))


print(combination(20, 20))

