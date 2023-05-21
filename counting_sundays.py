"""
Вам предоставлена следующая информация, но вы можете предпочесть провести исследование самостоятельно.

1 января 1900 года был понедельник.
Тридцать дней имеет сентябрь,
апрель, июнь и ноябрь.
У всех остальных - тридцать один,
За исключением одного февраля,
В котором двадцать восемь, дождь или солнце.
А в високосные годы - двадцать девять.
Високосный год бывает в любом году, который делится на 4, но не в столетии, если оно не делится на 400.
Сколько воскресений выпало на первое число месяца в двадцатом веке (с 1 января 1901 года по 31 декабря 2000 года)?
"""

import datetime


def option() -> int:
    c=0

    for i in range(1901, 2000+1):
        for j in range(1, 12+1):
            if datetime.date(i, j, 1).weekday()==6: #если понедельние то +1
                print(datetime.date(i,j,1))
                c+=1
    print(c)
    return c


def option1():
    months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    count=0
    day=2 # день недели первого января 1901 года
    for i in range(1901, 2001):
        if i%4==0 and i%100!=0 or i%400==0:
            months[1]=29
        else:
            months[1]=28

        for j in range(0, 12):
            day+=months[j]%7
            if day%7==0:
                count+=1
                print(datetime.date.fromisoformat(str(datetime.date(i,j+1,day%7+1))))
    print(count)




if __name__=='__main__':
    option1()
    #print(option())




#days=0
#for i in range(1901, 2000):
#    if i%4==0:
#        v=29
#    else:
#        v=28
#
#    # январь
#    for j in range(1, 30+2):
#        days+=j
#
#    # февраль
#    for j in range(1, v):
#        days+=j
#
#    # март
#    for j in range(1, 30+2):
#        days+=j
#        
#    # апрель
#    for j in range(1, 30+1): #
#        days+=j
#
#    # май
#    for j in range(1, 30+2):
#        days+=j
#
#    # июнь
#    for j in range(1, 30+1): #
#        days+=j
#
#    # июль
#    for j in range(1, 30+2):
#        days+=j
#
#    # август
#    for j in range(1, 30+2):
#        days+=j
#
#    # сентябрь
#    for j in range(1, 30+1): #
#        days+=j
#
#    # октябрь
#    for j in range(1, 30+2):
#        days+=j
#
#    # ноябрь
#    for j in range(1, 30+1): #
#        days+=j
#
#    # декабрь
#    for j in range(1, 30+2):
#        days+=j
#
#
#
#
#
#
