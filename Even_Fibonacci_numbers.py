
end=4000000
next_value=0


def fak(n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return fak(n-1)+fak(n-2)

def count_up(n):
    one = fak(n)
    two = fak(n+1)

    summ=two # 2

    

    def next(one, two, summ):
        value=one+two # получаем следующие число

        if value%2==0:
            summ+=value

        if value <= end:
            next(two, value, summ)
        else:
            print(summ)
            

    return next(one, two, summ)






if __name__=='__main__':
    count_up(1)


