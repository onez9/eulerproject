

def erst(num:int):
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
    return [i for i in range(len(arr)) if arr[i]==1]

def bin_search(num, arr):
    start=0; end=len(arr)
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

def solution():
    import functools

    n=50
    arr=erst(n)
    print(arr)






if __name__=='__main__':
    solution()