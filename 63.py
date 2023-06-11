
n=1
count=0
while n<=9:
    i=1
    while True:
        # print(i)
        if len(str(n**i)) != i:
            # print()
            break
        if i==len(str(n**i)):
            count+=1
            print(f'{count}) {n}**{i}={n**i}')
            # break
        i+=1
    # print()
    # print(f'n: {n}, i: {i}')
    n+=1


print(f'res: {count}')