# symbology solver

import numpy as np

symbols = ["circle", "cross","pentagon", "square", "star"]


def puzzle_one_twelve():
    # circle, cross, pentagon, square, star
    A = np.array([
        [3, 1, 0, 1, 0],
        [1, 0, 0, 2, 2],
        [2, 1, 0, 1, 1],
        [1, 0, 1, 1, 2],
        [2, 2, 1, 0, 0],
        [1, 1, 0, 2, 1],
        [2, 1, 1, 0, 1],
        [2, 1, 1, 1, 0],
        [3, 0, 0, 1, 1],
        [1, 1, 0, 1, 2],
    ])
    b = np.array([20, 24, 24, 20, 23, 27, 20, 19, 17, 28])

    # A * z = b
    z = np.linalg.lstsq(A,b, rcond=None)[0]
    out = zip(symbols,z)
    for (sym, val) in out:
        print(f"{sym}: {round(val)}")


def main():
    puzzle_one_twelve()

if __name__ == "__main__":
    main()