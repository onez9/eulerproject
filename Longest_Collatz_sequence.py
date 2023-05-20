


def count_up(n):
    count=1
    while not n==1:
        if n%2==0:
            #print(n)
            n=n>>1
        else:
            #print(n)
            n=3*n+1

        count+=1

    return count

limit=1e6
i=1
result=0
while i<limit:
    m=count_up(i)
    if result < m:
        result=m
        print(i, m)
    i+=1




