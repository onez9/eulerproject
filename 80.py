



from decimal import *

from math import sqrt

getcontext().prec = 102


def digitalsum(n):
    sum = 0
    for a in n:
        sum += int(a)
    return sum

total = 0

for a in range(100):
    if not sqrt(a) % 1 == 0:
        ans = str(Decimal(a).sqrt()).replace('.', '')[:100]
        print(a)
        print(digitalsum(ans))
        print("-------")


#from __future__ import print_function    #for python2 compatibility.
#
#from math import sqrt
#from decimal import Decimal, getcontext
#
#
#getcontext().prec = 102
#
#total = 0
#for a in range(100):
#    if not sqrt(a) % 1 == 0:
#        ans = str(Decimal(a).sqrt()).replace('.', '')[:100]
#        digits = map(int, ans)
#        print(a, sum(digits), "--------", sep='\n')
#
#        total += sum(digits)
#print(total)
