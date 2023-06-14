


def erst(n):
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
    return [ i for i in range(len(arr)) if arr[i]==1 and i>999 ]

def split_number(num):
    res=[]
    while num>0:
        res.append(num%10)
        num//=10
    return res[::-1]

def isPrime(num):
    i=2
    while i<num:
        if num%i==0:
            return False
        i+=1
    return True

def bin_search(num, arr):

    start=0; end=len(arr)

    # if num < min(arr) or num > max(arr):
    #     return -1

    while start<=end:
        index_search=(start+end)//2
        # print(start, end)
        if abs(start-end)==1:
            return False
        if num > arr[index_search]: #наше число больше середины
            start=index_search; 
        elif num < arr[index_search]:
            end=index_search
        else:
            return True

        



def norm_number(n1, n2, n3, arr):
    if bin_search(n2, arr) and bin_search(n3, arr):
        l1=sorted(split_number(n1))
        l2=sorted(split_number(n2))
        l3=sorted(split_number(n3))

        if l1==l2==l3:
            return True
        else:
            return False
    else:
        return False

def solution()->str:

    arr=erst(10000)
    for item in arr:
        v=item
        v1=1
        # print(item)
        while v+v1+v1<10000:
            # print(v, v1)
            if norm_number(v, v+v1, v+v1+v1, arr):
                print(v, v+v1, v+v1+v1)
                # yield (v, v+v1, v+v1+v1)
                yield f'{v}{v+v1}{v+v1+v1}'
            v1+=1

if __name__=="__main__":
    # print(split_number(2348))
    f=solution()
    print(next(f))
    print(next(f))
    # print(isPrime(13))
    # import random

    # arr=sorted([random.randint(10, 40) for _ in range(21)])
    # print(arr)
    # print(bin_search(15, arr))
    

        




