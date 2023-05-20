#from functools import L


def check(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True


def func(n):
    acc=0 # счётчик простых чисел
    count=0 # счётчик чисел


    while True:
        if check(count): # проверка на простое число
            print(f'{acc}: {count}')
            acc+=1

            if acc > n: # считаем сколько уже простых чисел нашли
                break

        count+=1

#def func(n):
    #input_arr=[1 for _ in range(1, n+1)]


    #i=2
    #input_arr[i]=0
    #while i <= n:
    #    j=i+i

    #    while j < n:
    #        input_arr[j]=0
    #        j+=i
    #    i+=1

    #print(input_arr)
    #return input_arr



        

if __name__=='__main__':
    n=100
    func(10001)
    #for i, item in enumerate(func(n)):
    #    if not item==0: 
    #        print(i, item) 

