#digit with powers

def func(n:int)->bool:
    tmp=n
    sum=0
    while tmp > 0:
        num=tmp%10
        sum+=num**3
        tmp//=10

    return True if sum==n else False



i=2
sum=0

print(9**5+8**5+7**5)
print(9**4+8**4+7**4)
print(9**3)
while i<=999:

    if func(i): sum+=i
        
    i+=1
print(sum)
