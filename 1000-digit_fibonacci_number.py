
i1=1
i2=1
count=3
while True:
    next_item=i1+i2
    print(count)
    i1=i2
    i2=next_item

    if len(str(next_item))==1000:
        break
    count+=1
    

