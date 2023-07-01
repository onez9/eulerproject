


import functools
import itertools


def solution(n: int) -> None:
    x0=0
    y0=0
    acc=0 # счётчик результатов
    res=set() # кортеж с результатами
    for x1, y1 in itertools.product(range(0, n+1), range(0, n+1)):
        for x2, y2 in itertools.product(range(0, n+1), range(0, n+1)):
            # for x1 in range(0, n+1):
            #     for y1 in range(0, n+1):
            #         for x2 in range(x1, n+1):
            #             for y2 in range(y1, n+1):
                            

            if (x1==x0 and y1==y0) or (x2==x0 and y2==y0) or (x1==x2 and y1==y2):
                # print('error: ', end=' ')
                continue

            # Находим координаты векторов
            x1_vec=x1-x0
            y1_vec=y1-y0

            x2_vec=x2-x0
            y2_vec=y2-y0

            x3_vec=x2-x1
            y3_vec=y2-y1

            
            # если какой-либо из 3 углов прямой то +1 к решению
            if x1_vec*x2_vec + y1_vec*y2_vec==0 or x1_vec*x3_vec + y1_vec*y3_vec==0 or x2_vec*x3_vec + y2_vec*y3_vec==0:
                # print(acc, ") ", x0, y0, " ", x1, y1, " ", x2, y2)
                
                # if x1==y2 and x2==y1:
                    
                #     res.add((x0,y0,min(x1,y1),max(x1,y1),max(x2,y2),min(x2,y2)))
                # else:

                # таким образом избавляемся от дубликатов между первой и второй точкой
                point1=min((x1,y1), (x2,y2))
                point2=max((x1,y1), (x2,y2))
                res.add((*point1, *point2))

                # res.add((x1,y1, x2,y2))

                
                acc+=1
    return res

if __name__=='__main__':
    for i, item in enumerate(solution(2)):
        print(i+1, item)
            
            # print()
    # print(len(list(res)))
    # print(len(res)+1)2