
d1 = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve'
}

d2 = {
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',   
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}


d3={
    20: 'twenty', 
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

d4={
    1e2: 'hundred',
    1e3: 'thousand',
    1e6: 'million',
}
#print(d4.get(1e2))
#print(d4[1e2])

d = d1 | d2 # python 3.9
d = {**d, **d3} #python 3.5
d.update(d4)




def check(num):
    res=0

    thousand=num//1000
    hundred=(num%1000)//100
    dozens=((num%100)//10)*10

    units=num%10
    dec_uni=num%100


    string=''


    #if d.get(num, False):
    #    print(num, d.get(num), len(d.get(num)))
    #    return len(d.get(num))
    if not thousand==0:
        res += len(d.get(thousand)) + len(d.get(1e3)) 
        string += d.get(thousand)+" "+d.get(1e3)+" "

    if not hundred==0:
        #print(hundred)
        res += len(d.get(hundred)) + len(d.get(1e2)) 
        string += d.get(hundred)+" "+d.get(1e2)+" "

    if dec_uni<20:
        #print(dec_uni)
        if not (hundred==0 or dec_uni==0):
            res+=3
            string+="and "

        #print(dec_uni)
        res+=len(d.get(dec_uni, ""))
        string += d.get(dec_uni, "")
        #print(dec_uni)


        print(num, string, res)
        return res
    else:
        #print(dozens, res)
        res+=len(d.get(dozens, "")) + len(d.get(units, ""))

        if not (hundred==0 or dec_uni==0):
            res+=3
            string+="and "


        string += d.get(dozens, "")+" "+d.get(units, "")
        print(num, string, res)
        return res



res=0
n=1000
for i in range(1, n+1):
    res+=check(i)
print(res)

#if num==1000:
#    res+=len(d[1]) + len(d[1000])
#    return res
#if num==100:
#    res+=len(d[1]) + len(d[100])
#    return res

#    if d.get(num, False):
#        res+=len(d[num])
#        return res
#    else:
#        hundreds=num//
#        num=str(num)
#        a=num[len(num)-2::]
#        if d.get(int(a), False):
#            res+=len(d[int(a)])
#        else:
#            b=num[len(num)-2:-1:]
#            c=num[len(num)-1::]
#            print(d.get(int(a)), d.get(int(b)), d.get(int(c)))
#            res+=len(d[int(b)*10]) + len(d[int(c)])
#    print(res)


    






