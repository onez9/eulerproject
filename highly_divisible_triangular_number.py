import sys
import math

#number=100
#tmp=number
#i=2
##print(math.sqrt(number))
#
#while i<math.sqrt(number):
#    while tmp%i==0:
#        tmp//=i
#        print(i, end=' ')
#    i += 1
#
#print()
#print(tmp)
#


nu=28
acc=2
next_summ=1
value=0
while True:
    #print(sum([item for item in range(acc)]))

    value += next_summ # проверяемое значение. именно у него мы смотрим делители

    sub_count=2
    product=1
    exit=False
    tmp_value=value
    while sub_count*sub_count<=tmp_value:
        c=1
        while tmp_value%sub_count==0:
            tmp_value//=sub_count
            c+=1

        sub_count+=1
        product*=c
        #print('product', product)

    if tmp_value==value or tmp_value>1:
        product*=2

    print(value, product)
    if product>nu:            
        #print(product)
        #print()
        break

    next_summ+=1 # это число на которое мы увеличим следущее проверяемое значение
    #acc+=1

