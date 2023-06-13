"""Find the value of d < 1000 for which 
1/d contains the longest recurring cycle 
in its decimal fraction part."""

from timeit import default_timer as timer
import math
from decimal import *
from functools import reduce
start = timer()

def longestPeriod(n): # define function
    longest = [0, 0] # length, num

    def isPrime(k): # checks if a # is prime
        for x in range(2, int(math.ceil(math.sqrt(k)))):
            if k % x == 0:
                return False
        return True

    def primeFact(k): # returns prime factorization of # in list
        if k <= 1: return []
        prime = next((x for x in range(2, 
            int(math.ceil(math.sqrt(k))+1)) if k%x == 0), k)

        return [prime] + primeFact(k//prime) 

    def periodIfPrime(k):
        period = 1
        while (10**period - 1) % k != 0:
            period += 1

        return period # returns period of 1/d if d is prime

    def lcm(numbers): # finds lcm of list of #s
        def __gcd(a, b):
            a = int(a)
            b = int(b)
            while b:
                a,b = b,a%b
            return a
        def __lcm(a, b):
            return ( a * b ) / __gcd(a, b)

        return reduce(__lcm, numbers)

    for x in range(3, n): # check all up to d for 1/d

        if all(p == 2 or p == 5 for p in primeFact(x)) == True: # doesn't repeat
            pass

        elif isPrime(x) is True: # run prime function
            if longest[0] < periodIfPrime(x):
                longest = [periodIfPrime(x), x]

        elif len(primeFact(x)) == 2 and primeFact(x)[0] == primeFact(x)[1]:
            if x == 3 or x == 487 or x == 56598313: # exceptions
                period = int(math.sqrt(x))
            else: # square of prime
                period = periodIfPrime(primeFact(x)[0]) * x
                if period > longest:
                    longest = [period, x]

        else:
            fact = primeFact(x)
            periods = []
            for k in fact:
                if k != 2 and k != 5:
                    if fact.count(k) == 1:
                        periods.append(periodIfPrime(k))
                    else:
                        periods.append((periodIfPrime(k)) * k**(fact.count(k) - 1))

            if lcm(periods) > longest[0]:
                longest = [lcm(periods), x] 

            return longest

elapsed_time = timer() - start
elapsed_time /= 100 # milliseconds

print("Found %d in %r ms." % (longestPeriod(1000)[1], elapsed_time))