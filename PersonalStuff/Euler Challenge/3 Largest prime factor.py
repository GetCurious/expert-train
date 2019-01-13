"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

n = 600851475143
i = 2
while i * i < n:
    while n%i == 0:
        n = n // i
    i = i + 1
print (n)

#########################

from math import sqrt
primes = set([2])
value = 3
number = 600851475143
while value < sqrt(number):
    isPrime = True
    for k in primes:
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        primes.add(value)
        if number % value == 0:
            print (value)
            number /= value
print (number)
