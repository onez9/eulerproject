import logging
from itertools import product



n=1001
xc=n//2
yc=n//2
path=n*n-1

arr=[[0]*n for _ in range(n)]
arr[yc][xc]=1
xc+=1
arr[yc][xc]=2
length=1
acc=3
rt=0
while acc<n*n:
    for i in range(length):
        yc+=1
        arr[yc][xc]=acc
        acc+=1

    length+=1
    for i in range(length):
        xc-=1
        arr[yc][xc]=acc
        acc+=1
    for i in range(length):
        yc-=1
        arr[yc][xc]=acc
        acc+=1

    if rt==n//2-1:
        length-=1


    length+=1
    for i in range(length):
        xc+=1
        arr[yc][xc]=acc
        acc+=1

    rt+=1


print(*arr, sep='\n')




res=0
for y,x in product(range(n), range(n)):
    if y==x or y==n-x-1:
        res+=arr[y][x]


print(res)


