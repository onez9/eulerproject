from itertools import product

res=set()
n=5
for a in range(2, n+1):
    for b in range(2, n+1):
        print(a**b, sep=' ')
        res.add(a**b)
    print()

print(len(res))
#print(sorted(res))
