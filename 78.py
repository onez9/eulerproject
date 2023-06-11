




# рекурентный вариант
# def Pr(n:int,k:int)->int:
#     if k==0 and n==0:
#         return 1
#     if k==0 and n>0:
#         return 0
#     if n>=k:
#         return Pr(n,k-1) + Pr(n-k, k)
#     if n<k:
#         return Pr(n, n)

def generate(n:int)->int:
    gk= (3*n**2-n)//2
    return gk

def pentagonal(N):
    a, b = 1, 2
    delta = 4
    sgn = 1
    while a <= N:
        yield sgn, a
        a += delta
        if b <= N:
            yield sgn, b
            b += delta + 1
        delta += 3
        sgn = -sgn


if __name__=='__main__':


    # for sgn, g in pentagonal(20):
    #     print(sgn, g)
    P={}
    modulus = 1e6
    P[0] = 1
    n = 0
    while P[n] != 0:
        n += 1
        # print(n)
        P[n] = 0
        for sgn, g in pentagonal(n):
            print(sgn, g)
            P[n] += sgn * P[n-g]
            # print(P[n])
            P[n] %= modulus
    print(n)







    # for i in range(100):
    #     print(1+i//2)
    #     # if i%4<2:
    #     #     print(1, 2)
    #     # else:
    #     #     print(3,4)
    # i=1
    # n=3
    # res=1
    # k=1
    # p=1
    # while True:
    #     p*=1/(1-) 
        
    #     k+=1

    # partitions=[]
    # partitions.append(1)
    # limit=1e5
    # modulo=1e6

    # n=len(partitions)

    # while n<=limit:
    #     sum=0
    #     i=0
    #     while True:
    #         alternative=1+i//2
    #         if i%2==1: alternative=-alternative
            
    #         offset=alternative*(3*alternative-1)//2

 
    #         if n<offset: break

    #         if i%4<2: sum+=partitions[n-offset]
    #         else: sum-=partitions[n-offset]
    #         print(sum)
    #         # sum%=modulo
    #         i+=1
        
    #     if sum<0: sum+=modulo
    #     if sum==0: break
    #     partitions.append(sum)



    # print(len(partitions))

    # print(res)
    # while i<=n:
    #     g1=generate(-i)
    #     g2=generate(i)

    #     res += n**g1 + n**g2

    #     res += -(n**g1 + n**g2)
    #     i+=1



