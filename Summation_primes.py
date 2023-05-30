

# Решето Эрстофена
def func(n):
    arr=[1 for _ in range(n)]

    arr[0]=0
    arr[1]=0

    i=2
    arr[i]=1

    while i<n:
        j=i+i
        while j<n:
            arr[j]=0
            j+=i
        i+=1


    return arr


if __name__=='__main__':
    n=2*10**6
    #n=10
    summ=0
    for i, item in enumerate(func(n)):
        if item!=0:
            print(i, item)
            summ += i
    print(summ)

