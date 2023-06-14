

def erst(num:int)->[]:
    arr=[1 for _ in range(num)]
    arr[0]=0
    arr[1]=0
    i=2
    arr[i]=1
    while i<num:
        j=i+i
        while j<num:
            arr[j]=0
            j+=i
        i+=1
    return [i for i in arr if arr[i]==1]

def solution()->None:
    print(erst(100))


if __name__=='__main__':
    solution()