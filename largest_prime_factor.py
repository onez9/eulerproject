import sys




def func2(prime, lst):
    if not len(lst)==0:
        if not prime%lst[0]==0:
            return func2(prime, lst[1:])
        else:
            prime+=lst[0]
    return prime



def func(n, prime, lst):
    if not n==1:
        if n%prime==0:
            # тут мы должны предположить какое приблиз
            lst.append(prime)

            #func2(prime, lst)
            
            func(n/prime,prime,lst)
        else:
            if (prime+1)%2==0:
                func(n,prime+2,lst)
            else:
                func(n,prime+1, lst)
    else:
        print(prime-1)
        print(lst)





if __name__=='__main__':
    sys.setrecursionlimit(20000)
    print('предел хвостовой рекурсии: ', sys.getrecursionlimit())



    n = 13195
    n = 600851475143
    #n = 52
    prime=2
    lst=[]
    func(n, prime, lst)
