import functools




class solution:
    def __init__(self):
        ...

    # good
    def phi1(self, n: int)->list:
        c=2;result=n
        while c*c<=n:
            if n%c==0:
                while n%c==0:
                    n//=c; #res.append(c)
                result-=result//c
            c+=1
        
        if n>1:
            result-=result//n
        # return res
        return result

    # bad
    def phi2(self, n: int)->None:
        res=[]
        for i in range(1, n):
            if self.gcd(i, n) == 1:
                res.append(i)
        # print(res)
        return len(res)
        # return res


    def gcd(self, a: int, b: int)->int:
        while True:
            if a == 0 or b == 0:
                return a + b
            if a > b: 
                a = a % b
            else: 
                b = b % a






if __name__=='__main__':
    # print(gcd(8, 9))
    n=1000000
    s=solution()
    print(functools.reduce(max, [ i/s.phi1(i) for i in range(2, n) ]))
    mx=0;res=0
    for i in range(2, n+1):
        current = i/s.phi1(i)
        if mx < current:
            mx=current
            res=i

    print(res)


    # print(s.phi1(1000000))
    # print(s.phi2(1000000))
    # print(phi(n))