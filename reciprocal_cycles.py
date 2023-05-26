#e=1000
#i=1
#digit=100
#while i<=e:
#    #print(f"{1/i:.{digit}f}")
#    print(float('{:.100f}'.format(1/i)))
#    i+=1


def cycleLength(b):
    a = 1
    t = 0
    arr=[]
    c=0
    while a not in arr:
        print(a*10//b)

        arr.append(a*10%b)
        a = a * 10 % b
        t+=1
        #print(a)
        if (a==0):
            break
        
        
        
        c+=1
    #print(123)
    print(arr)
    return t

t=int(input('type value: '))
print(cycleLength(t))

#print(1/7)
#def solution():
#    max = 0
#    max_p = 0
#
#    for d in range(1,1000):
#        tmp = cycleLength(d)
#        if (max < tmp):
#            max_p = d
#            max = tmp
#        print(d)
#      
#    
#    return max_p;
#
#solution()


