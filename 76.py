






if __name__=='__main__':
    print('start')

    print("arr")
    target = 5
    ns = range(1, target)
    ways = [1] + [0]*target

    for n in ns:
        for i in range(n, target+1):
            ways[i] += ways[i-n]

    print("Number of ways", target, "can be written as a \nsum of at least two positive integers:", ways[target])



