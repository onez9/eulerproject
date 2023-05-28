import functools
import itertools



def fuck(n:int)->int:
    i=1
    s=1
    while i<=n:
        s*=i
        #print(s)
        i+=1
    return s



s=1
i=3
res=0
#print(fack(8))
while i<1000000:
    t1=i
    t2=sum([fuck(int(item)) for item in str(i)])
    if t1==t2:
        print(t1, t2)
        res+=t1
    i+=1

print(res)

    #break
    











