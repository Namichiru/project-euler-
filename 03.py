"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

result = 1
x = 2
b, c = 600851475143, 600851475143
while c > result:
    if b % x == 0:
        b = b / x
        result *= x
        print('prime factor is:', x, 'result is:', result)
        x = 2
    else:
        x += 1
