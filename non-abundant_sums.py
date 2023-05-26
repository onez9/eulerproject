import math
import itertools


def getDivisorzSum(num: int) -> int:
    sum=0
    #for i in range(2, int(math.sqrt(num))):
    i=2
    while i*i < num:
        if num%i==0:
            sum+=i+num//i
        i+=1

    if i*i==num:
        sum+=i

    sum+=1

    return sum

def isAbundant(num: int) -> bool:
    if getDivisorzSum(num)>num:
        return True
    else:
        return False


if __name__=='__main__':
    LIMIT=28123
    abundantNums=[]
    for i in range(12, LIMIT+1):
        if isAbundant(i):
            abundantNums.append(i)
    #del abundantNums[0]

    sums=[0]*(LIMIT+1)
    #print(abundantNums)

    for i in range(len(abundantNums)):
        for j in range(i, len(abundantNums)):
            #if (abundantNums[i]+abundantNums[j])>LIMIT: 
            #    break
            sumof2abundans=abundantNums[i]+abundantNums[j]
            if sumof2abundans<=LIMIT and sums[sumof2abundans]==0: 
                sums[sumof2abundans]=sumof2abundans

    total=0
    for i in range(1, len(sums)):
        if sums[i]==0:
            total+=i

    #total=sum(itertools.compress(range(1, LIMIT+1), sums))
    print(total)





#r=isAboundant(12)
#print(r)









#limit=28123
#num=int(input("Введите число: "))
#sum=0
#j=3
#res=0
#while j<=limit:
#    num=j
#
#    if sum==num:
#        print(f'число {num} - идеальное, sum = {sum}')
#        res+=num
#    #if sum>num:
#    #    print(f'число {num} - избыточное, sum = {sum}')
#    if sum<num:
#        res+=num
#        print(f'число {num} - недостаточное, sum = {sum}')
#    j+=1
#print(res)


