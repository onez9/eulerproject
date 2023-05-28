

# d1={
#         1:'I',
#         2:'II',
#         3:'III',
#         4:'IV',
#         5:'V',
#         6:'VI',
#         7:'VII',
#         8:'VIII',
#         9:'IX',
#         10:'X',
#         20:'XX',
#         30:'XXX',
#         40:'XL',
#         60:'LX',
#         70:'LXX',
#         80:'LXXX',
#         90:'XC',
#         50:'L',
#         100:'C',
#         500:'D',
#         600:'DC',
#         700:'DCC',
#         800:'DCCC',
#         900:'CM',
#         1000:'M',
# }


with open('p089_roman.txt') as fi:
    import itertools
    import logging

    # level=logging.WARNING
    # logging.basicConfig(level=logging.WARNING)

    res_end=0
    for item in fi.read().split('\n'):
        result=[]
        r1=''
        # f1=f2=f3=f4=f5=f6=f7=False
        thousand=hundred=dec=unit=0
        # gr = list(itertools.groupby(item))
        # item='MMCXCIV'
        for it, arr in itertools.groupby(item):
            # l=len(list(gr[i][1]))
            l=len(list(arr))
            # it=gr[i][0]
 

            if it=='M':
                result.append(l*1000)
                # print(result)
            if it=='D':
                result.append(l*500)
                # print(result)
                # if f3:
                #     result += -hundred + l*500 
                # else:
                #     result += l*500
                
            if it=='C':
                result.append(l*100)
                # print(result)
                # if not (gr[i+1][0]=='M' or gr[i+1][0]=='D'):
                #     result+=l*100
                # f3=True
            if it=='L':
                result.append(l*50)
                # print(result)
            if it=='X':
                result.append(l*10)
                # print(result)
                # f5=True
            if it =='V':
                result.append(l*5)
                # print(result)
                # f6=True
            if it =='I':
                result.append(l)
                # print(result)
                f7=True
        #logging.warning(res)
        #break

        # print(result)
        # res=result[]
        for i in range(0, len(result)-1):
            if result[i] < result[i+1]:
                result[i]*=-1
        # print(list(map(lambda x, y: xy, result)))
        # result = [ -result[i] if result[i] < result[i+1] else result[i] for i in range(len(result)-1) ]
        # print(result)
        # print(sum(result))



        # t=sum([result[i]-result[i-1] if result[i]>result[i-1] else result[i] for i in range(1, len(result))])
        # print(t)
        
        t=sum(result)
        # t=5370
        # break
        #t=int(input('type number: '))
        # print(t)
        
        if t>1000:
            r1+='M'*(t//1000)

        hund=t%1000//100
        if hund==9:
            r1+='CM'
        elif hund==4:
            r1+='CD'
        elif hund > 4 and hund<9:
            r1+= 'D'+'C'*(hund % 5)
        elif hund > 0 and hund < 4:
            r1+='C'*hund

        dec=t%100//10
        if (dec==9):
            r1+='XC'
        elif (dec==4):
            r1+='XL'
        elif dec < 9 and dec > 4:
            r1+='L'+('X'*(dec%5))
        elif dec > 0 and dec < 4:
            r1+='X'*dec
            

        unit=t%10
        if unit==9:
            r1+='IX'
        elif unit==4:
            r1+='IV'
        elif unit > 4 and unit < 9:
            r1+='V'+'I'*(unit%5)
        elif unit>0 and unit<4:
            r1+='I'*unit


        print(f'my {r1}, base: {item}, dec: {t}')
        res_end+=len(item)-len(r1)
        # break
    print(res_end)





