import re
import itertools
import functools

#digit=100
#while i<=e:
#    #print(f"{1/i:.{digit}f}")
#    print(float('{:.100f}'.format(1/i)))
#    i+=1
# i=2
# while i <= 1000:
#     i+=1


# def check(arr):
#     ch=''
#     import re
#     input=''.join(map(str, arr))[2::]
#     for i in range(len(input)):
#         # if input[::]==input[::]:
#         if input[i]=='0':
#             return True

def sub_func(divider):
    multiple = 1 # кратное, делитель
    while True:
        number = multiple * 10 // divider # результат # делитель
        multiple = multiple * 10 % divider # остаток
        yield (str(multiple), str(number))



def decigion1(divider):
    fuck=sub_func(divider)
    if divider==1:
        # print(1)
        return 1
    # elif divider%2==0:
    #     # print(0)
    #     return 0

    t=0
    tmp=0
    total=''
    acc=0
    enable=0
    count=0
    while True:
        multiple, number = next(fuck)
        
        if number!='0' or enable==1:
            enable=1
            total+=number
            # print(number, end='')

        
            if tmp==multiple:
                count+=1
                if count==2:
                    break

        
        if t>2:

            if total[acc]==number: 
                acc+=1

                if acc==len(total)/2:
                    break
                    # return acc
            else:
                acc=0

        t+=1
        tmp=multiple
    # print()
    return acc


def decigion2(b):
    a=1
    t=0
    while True:
        a=a*10%b
        t+=1
        if a==1:
            break
    return t

def reciprocal_cycles(divider):
    multiple = 1 # кратное, делитель
    count=0
    while True:
        # number = multiple * 10 // divider # результат # делитель
        multiple = multiple * 10 % divider # остаток
        # yield (str(multiple), str(number))
        count+=1
        if not multiple==1:
            break
    return count


def erstafen_func(n):
    arr=[1 for _ in range(n)]
    arr[0]=0
    arr[1]=0
    i=2
    arr[i]=1
    while i<n:
        j=i*2
        while j<n:
            arr[j]=0
            j+=i
        i+=1
    return arr

# print(erstafen_func(1000))
# arr=[]


# max_len=0
# result=0
# for i, item in enumerate(erstafen_func(1000)):
#     if item==1:
#         v=decigion1(i) 
#         # t_i=i
#         if v > max_len:
#             max_len=v
#             result=i
# print(result, max_len)


# filter(lambda x: x==1, )
# print(decigion1(7))
arr=[ (decigion1(i), i) for i, item in enumerate(erstafen_func(1000)) if item==1 ]
tmax=0
res=0
for l, n in arr:
    if tmax<l:
        tmax=l
        res=n
print(res)

# for i in range(len(arr)-1):
#     print(functools.reduce(max, arr[i], arr[i+1]))




# print()
# for i in range(2, 100):
#     print(f'{i}) {decigion1(i)}')
# print()

# t=int(input('Введите число: '))

# import itertools
# while acc<=10:
#     print(acc,'\t', decigion(acc))
#     # acc+=1


# from lib.sequence import Primes


# print(Primes(upper_bound=1000))
