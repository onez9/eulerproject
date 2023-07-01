

def get_fac(n:int)->None:
    i=2; res=[]; tmp_n=n
    while tmp_n>1:
        # print(i)
        while tmp_n%i==0: 
            res.append(i)
            tmp_n//=i
        i+=1
    return res

def solution(n: int)->None:
    # total=1000
    result=0
    t=0
    # while True:
        
        
    #     t+=1

    
    # return result



    for total in range(n, 1, -1):
        for blue in range(int(total), 1, -1):
            if blue/(total) * (blue-1)/(total-1) == 0.5:
                print(f'{blue}: {get_fac(blue)}, {total}: {get_fac(total)}')
                # print(f'{blue-1}: {get_fac(blue-1)}, {total-1}: {get_fac(total-1)}')
                # print(blue, total)
                break
            



if __name__=='__main__':
    n=int(1e3)
    # n=int(input('Type value: '))
    # print(get_fac(n))


    solution(n)