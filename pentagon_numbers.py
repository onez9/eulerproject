

import math

def isPentagonal(n:int)->bool:
    d=1+math.sqrt(1+24*n)

    if d%6==0:
        return True
    else:
        return False



if __name__=="__main__":
    #print(math.sqrt(-1))
    k=1
    while True:
        pk=k*(3*k-1)//2
        k+=1
        for j in range(k+1, 5000):
            pj=j*(3*j-1)//2
            # x=n(3n-1)/2
            # 2x=n(3n-1)
            # 2x=3n^2-n
            # 3n^2-n-2x==0
            # n12=(1+-sqrt(1-4*3*2))/2*3
            if isPentagonal(abs(pk-pj)) and isPentagonal(abs(pk+pj)):
                #print(pk, pj, abs(pk-pj), abs(pk+pj))
                print(abs(pk-pj))
                break
        else:
            continue
        break


#i=0
#while i<=100:
#    n=i
#    pn=n*(3*n-1)//2
#    print(pn)
#
#
#    i+=1
