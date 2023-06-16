

def solution1():
    m=0
    for i in range(100):
        for j in range(100):
            s=sum(list(map(int, str(i**j))))
            if m<s:
                m=s
    return m

def solution2():
    ...

if __name__ == '__main__':
    ...
