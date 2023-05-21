
s=2
n=1e4

def d(n:int)->int:
    i=2
    sm=0
    num=n
    while i*i<num:
        if num%i==0:
            sm+=i+num//i
        i+=1
    sm+=1
    return sm

set1=set()
while s<n:
    if s==d(d(s)) and s!=d(s):
        set1.add(s)
        set1.add(d(s))


    s+=1

print(set1)
print(sum(set1))


