from math import sqrt, ceil, floor
from itertools import groupby

def up(n: int):
    return sqrt(n) + n


def down(n: int):
    return 1


def nod(n1: int, n2: int) -> int:
    if n1 == 0 or n2 == 0:
        return n1 + n2
    elif n1 < n2:
        return nod(n1, n2 % n1)
    elif n1 > n2:
        return nod(n1 % n2, n2)
    else:
        return n1


def get_phase():
    n = 2
    a = 1
    up = sqrt(n) - a
    down = 1
    whole_part = 0
    mn = 1
    phase = []
    i = 0

    print('')
    while i <= 13:
        up, down = down, up
        tmp_up = up
        up = (sqrt(n) + a)
        down = round(down * (sqrt(n) + a))

        print(tmp_up, down, mn)
        d = nod(tmp_up, down)
        # print(d)
        tmp_up //= d
        down //= d  # сокращаем дробь

        up = up * tmp_up

        # print(mn)
        if down == 1:
            # print('down==1')
            mn = a * 2
            up = sqrt(n) - a
        elif a < down:
            # print("a < down")
            mn = 1
            a = down - a
            up = sqrt(n) - a
        else:
            # print("a > down")
            mn = a
            a = a * down - a
            up = sqrt(n) - a

        phase.append(mn)
        # print(tmp_up, down)

        # print(nod(12, 16))
        # break

        i += 1
    return phase


def get_length(phase: list) -> int:
    i = 1
    acc = 0
    i1=0
    one1=False
    while True:

        while i1<=len(phase):
            if phase[0]!=phase[i]:
                one1=True
        if one1:
            return 1

        if i == 1:
            while phase[i] == phase[i + 1]:
                i += 1

        if phase[acc] == phase[i]:

            # print(f'phase[acc]: {phase[acc]}, acc: {acc}', end='\n')
            # print(phase[acc], end='')
            if acc == i / 2:
                # print(acc)d
                break
            acc += 1
        else:
            print()
            acc = 0

        i += 1
    return acc


if __name__ == '__main__':
    # p = get_phase()
    # print(p)
    # res = get_length(p)
    # print(res)

    items = groupby('hello world')
    for item, it in items:
        print(item, list(it))