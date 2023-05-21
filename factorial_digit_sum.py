


def fac(n: int) -> int:
    if n==1:
        return 1
    else:
        return fac(n-1)*n

def get_sum(n: int) -> int:
    if n==0:
        return 0
    else:
        return get_sum(n//10) + n%10

if __name__=='__main__':
    n = fac(100)
    print(n)
    #res=0
    #while n>0:
    #    res+=n%10
    #    n//=10
    res = get_sum(n)
    print(res)
