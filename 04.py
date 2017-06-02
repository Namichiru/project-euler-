"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.
"""

a = []
for x in range(100, 999):
    for y in range(100, 999):
        num = x * y
        if str(num) == str(num)[::-1]:
            a.append(num)
print(max(a))

