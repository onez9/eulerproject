
import re
import itertools





with open('p059_cipher.txt', mode='r') as fi:
    message=list(map(int, re.findall(r'\w+', fi.read())))
    # print(txt)
    l=len(message)
    keys=[chr(i)+chr(j)+chr(k) for i, j, k in  itertools.product(range(97, 97+26), range(97, 97+26), range(97, 97+26))]



    for i, key in enumerate(keys):
        open_text=''
        for j in range(l):
            open_text += chr(message[j]^ord(key[j%3]))
            # print(key[i%3])
        if not re.search(r'(?=.*on )(?=.*by )(?=.*taken)', open_text)==None:
            # if i==1454:
            print(sum([ord(k) for k in open_text]))
            break
