import io
import re

with io.open('p022_names.txt', mode='r') as fi:
    r=fi.read()
    r = re.findall(r"\w+", r)
    r = sorted(r)
    #print(*r, sep='\n')
    res = sum([ sum([ord(sym)-64 for sym in item])*(1+i) for i, item in enumerate(r) ])

    print(res)


