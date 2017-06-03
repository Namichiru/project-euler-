

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from math import sqrt

b = 1
for a in range(1, 400):
    c = a ** 2 + b ** 2
    if sqrt(c) == int(sqrt(c)):
        print('A is:', a, 'B is:', b, 'its:', c, 'ANSWER is:', a + b + sqrt(c), 'a*b*c =', a * b * sqrt(c))
        continue
    else:
        b += 2

