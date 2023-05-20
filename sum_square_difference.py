


def sum_of_squares(n, limit=10):
    if n < limit:
        return n**2 + sum_of_squares(n+1,limit)
    else:
        return n**2

def square_of_sum(n, limit=10):
    if n < limit:
        return n + square_of_sum(n+1,limit)
    else:
        return n


if __name__=='__main__':
    limit=100
    difference = (square_of_sum(1, limit)**2 - sum_of_squares(1, limit))
    print(difference)

