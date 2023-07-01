
# import re
import io
import math
import sys
import math

def fac(n:int)->None:
    i=2; res=[]; tmp_n=n
    while tmp_n>1:
        # print(i)
        while tmp_n%i==0: 
            res.append(i)
            tmp_n//=i
        i+=1
    return res


class result:
    def __init__(self, x=1, y=1, n=1):
        self.x=x
        self.y=y
        self.n=n


def solution()->int:
    acc=1
    mx=0;number=0;res=result()
    with io.open('p099_base_exp.txt', mode='r') as fi:
        while True:
            tx = fi.readline()
            
            if tx=='':
                break
            x, y = list(map(int, tx.split(',')))
            # print(fac(x), fac(y))
            current = y*math.log(x)
            if mx < current:
                mx = current 
                res.x = x; res.y = y; res.n=acc
                
            # if acc==6: break
            acc+=1
    print(mx)
    print(res.x, res.y, res.n)




if __name__=='__main__':
    solution()
    # sys.set_int_max_str_digits(3000000)


