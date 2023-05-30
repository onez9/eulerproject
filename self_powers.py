

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

def stupid_decigion()->int:
    n=1000
    i=1
    res=0
    mod=int(1e10)

    while i<=n:
        #print(i**i)
        #res+=powmod1(i, i, mod)

        res+=powmod1(i, i, mod)
        print(res)
        #res=res%mod

        i+=1

    #print(str(res)[-10::])
    #return str(res)[-10::]
    return res%mod

if __name__=='__main__':
    res=stupid_decigion()
    #print(9%2)
    #print((4%2 + 5%2))
    print(res)

