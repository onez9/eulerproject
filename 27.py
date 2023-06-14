





def erst(n: int):
    arr=[1 for _ in range(n)]
    arr[0]=0
    arr[1]=0
    i=2
    arr[i]=1
    while i<n:
        j=i*2
        while j<n:
            arr[j]=0
            j+=i
        i+=1
    return [i for i in range(len(arr)) if arr[i]==1]


# print(erst(1000000))

from time import sleep
import math

def iter1():
    n=0
    while True:
        n+=1
        yield n

def isPrime(num:int)->bool:
    i=2
    while i*i<=num:
        if num%i==0:
            return False
    return True

def countPrimes(a:int, b:int):
    f=iter1()
    for n in f:
        # print(n)
        c = n*n + a*n + b
        # print(a, b)
        if not isPrime(c):

            return n


if __name__=='__main__':
    v=0
    max=0
    arr=erst(1000)
    res=0
    print(arr)
    # sleep(5)
    for a in range(-999, 1000, 2):
        for i, b in enumerate(arr):
            v=countPrimes(a - 1 if i==0 else 0, b)
            # print(a, b, v)
            if max<v:
                max=v
                res=a*b
    print(max, res)



