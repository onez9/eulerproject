

def f1(n):
    tn=n*(n+1)/2
    return tn

def f2(n):
    pn=n*(3*n-1)/2
    return pn

def f3(n):
    hn=n*(2*n-1)
    return hn


def powmod1(x:int, y:int, n:int)->int:
    r=1
    while y!=0:
        #print(y)
        #if not y%2==0:
        if y&0x01:
            r=r*x%n
            #print('r: ', r, 'x: ', x)
        x=x*x%n
        y>>=1
    return r

def powmod2(x:int,y:int,n:int,r:int)->int:
    if y==0:
        return r
    if y&0x01:
        return powmod2(x*x%n,y>>1,n,(r*x)%n)
    return powmod2(x*x%n,y>>1,n,r)


if __name__=='__main__':
    y=130
    x=2
    n=87613813
    #print(n, b:=n>>1, n//2, b*2)
    print(powmod1(x,y,n))
    print(powmod2(x,y,n,1))
    print(pow(x,y,n))

    print(19 % 13)
    print(19 % -13)

    import math

    print(19 % -13, math.floor(19/12)) # down
    print(19 % -13, math.ceil(19/12)) # up


    print('как вычислить остаток от деления по модую от отрицательного числа: ', 19 % -12, 19 - round(19/-12)*-12) # up ~ down


    

#print(120&0x01)
#print(f1(285))
#print(f2(165))
#print(f3(143))





