




def right(r, d):
    print(r, d)
    if not r==0:
        right(r-1, d)
    if not d==0:
        down(d-1, r)


def down(d, r):
    print(r, d)
    if not r==0:
        right(r-1, d)
    if not d==0:
        down(d-1, r)

def calculate(r, d):
    if r==0 or d==0:
        return 1
    return calculate(r-1,d) + calculate(r,d-1)

# задача с маршрутами
def fac(n: int) -> int:
    res=1
    for i in range(1, n+1):
        res*=i
    return res


if __name__=='__main__':
    #res=0
    #res+=right(20, 20)
    #res+=down(20, 20)
    #print(res)

    #x=int(input('x: '))
    #y=int(input('y: '))
    #res=calculate(x,y)
    #print(res)
    n=int(input('n:'))

    print(fac(n*2)//(fac(n)*fac(n)))




    

