

def func():
    summ=1000 #a+b+c
    for a in range(1, summ):
        for b in range(a+1, summ):
            c=summ-b-a
            if a**2+b**2==c**2 and a < b < c and a+b+c==1000:
                print((a, b, c), a+b+c)
                return a*b*c

if __name__=='__main__':
    print(func())
