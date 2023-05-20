import sys
from functools import reduce

#def func(test_number, div):
#
#    while div<11:
#        print(test_number, div)
#        if test_number%div==0:
#            div+=1
#        else:
#            div=2
#            test_number+=1
#            print()
#
#    print(test_number)
#

def lcm(*values):
    print(values, values[0])
    values = [value for value in values]
    #print(values)
    if values:
        n = max(values)
        m = n
        values.remove(n) # удаляем последнее число
        #while any( n % value for value in values ): # если есть число хотябы одно число не кратное value то n+=m
        while n % values[0]: # если есть число хотябы одно число не кратное value то n+=m
            n +=m
            #print(n)

        return n
    return 0

if __name__=='__main__':
    # наименьшее общее кратное
    #sys.setrecursionlimit(20000)
    print('предел хвостовой рекурсии: ', sys.getrecursionlimit())
    print(reduce(lcm, range(1,21)))
