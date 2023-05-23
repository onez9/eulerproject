import math


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


abundantNums=[]
for i in range(28123+1):
    if isAbundant(i):
        abundantNums.append(i)

del abundantNums[0]


sums=[0]*28124
for i in range(len(abundantNums)):
    for j in range(i, len(abundantNums)):
        sumOf2abunds= abundantNums[i]+abundantNums[j]
        if sumOf2abunds<=28123 and sums[sumOf2abunds]==0:
            sums[sumOf2abunds]=sumOf2abunds

total=0
for i in range(1, len(sums)):
    if (sums[i]==0):
        total+=i
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


