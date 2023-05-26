import itertools


arr=[0,1,2,3,4,5,6,7,8,9]

iter1=itertools.permutations(arr)
start=999999
end=start+1
step=1
tmp=itertools.islice(iter1, start, end, step)
#print([i for i in tmp[0]])
print("".join([str(i) for i in next(tmp)]))
#print(next(tmp))
#print(next(tmp))
#print(next(tmp))
#print(next(tmp))
#print(...)




