import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def gcd(a, b):
    c = min(a, b)
    for num in range(c, 0, -1):
        if a % num == 0 and b % num == 0:
            return num
    return 1


if __name__ == '__main__':

    grid_size = 50
    straight = 3*(grid_size**2)

    diagonals = 0
    for x in range(1, grid_size+1):
        for y in range(1, grid_size+1):
            length = x
            divisor = gcd(x, y)
            horizontal_jump = y/divisor
            vertical_jump = x/divisor
            for j in range(0, int(y/vertical_jump)):
                length += horizontal_jump
                if j == int(y/vertical_jump)-1 and length <= grid_size:
                    diagonals += (j + 1)
                    break
                if length > grid_size:
                    diagonals += j
                    break

    # mirror around the diagonal
    diagonals *= 2

    logging.info(f"{straight + diagonals} triangles with a right angle can be constructed on a "
                 f"{grid_size} by {grid_size} grid")