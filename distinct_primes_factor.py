
def fuck(n:int)->[]:
    tmp=n
    i=2
    arr=[]
    while tmp>1:
        while tmp%i==0:
            tmp//=i
            arr.append(i)
            #arr.append(tmp//i)
            #print(i)
        #print(tmp)
        i+=1

    return sorted(arr)


if __name__=='__main__':
    #n=int(input())
    import itertools
    i=644
    while i<=9999:
        #print(fuck(i))
        item=fuck(i)
        if(len(set(item)))==4:
            print(i, sorted(set(item)), list(next(itertools.groupby(item))[1]))
        i+=1

