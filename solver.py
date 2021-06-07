# symbology solver

import argparse
import numpy as np

sym_map = {"C":"● ", "X":"✚ ", "P":"⬟ ", "S":"■ ", "R":"★ "}

def parse_opts():
    parser = argparse.ArgumentParser(description='Solve Symbolism puzzles.')
    parser.add_argument('filename', metavar='filename', type=str)
    return parser.parse_args()

def parse_file(filename):
    puzzle = []
    with open(filename, "r") as f:
        for line in f:
            puzzle_line, puzzle_val = [], 0
            for c in line:
                if c == " ":
                    if puzzle_val != 0:
                        puzzle_line.append(puzzle_val)
                    puzzle_val = 0
                if c in sym_map:
                    puzzle_line.append(c)
                if c in "0123456789":
                    puzzle_val = puzzle_val * 10 + int(c)
            puzzle_line.append(puzzle_val)
            puzzle.append(puzzle_line)
    return puzzle

def puzzle_print(puzzle):
    for x in range(5):
        for y in range(5):
            print(sym_map[puzzle[x][y]],end='')
        print()
    print()

def convert(puzzle):
    A, b = [], []
    for x in range(5): # for every line
        count = {"C":0, "X":0, "P":0, "S":0, "R":0}
        for y in range(5):
            c = puzzle[x][y]
            count[c] += 1
        A.append(list(count.values()))

    for y in range(5): # for every row
        count = {"C":0, "X":0, "P":0, "S":0, "R":0}
        for x in range(5):
            c = puzzle[x][y]
            count[c] += 1
        A.append(list(count.values()))

    for i in range(5):
        val = puzzle[i][5]
        b.append(val)

    for i in range(5):
        val= puzzle[5][i]
        b.append(val)
    return (A, b)

def solve(A, b):
    A = np.array(A)
    b = np.array(b)
    z = np.linalg.lstsq(A, b, rcond=None)[0]
    return z

def write_solution(z):
    out = zip(["circle", "cross","pentagon", "square", "star"], z)
    for (sym, val) in out:
        print(f"{sym}: {round(val)}")

def main():
    args = parse_opts()
    puzzle = parse_file(args.filename)
    puzzle_print(puzzle)
    (A, b) = convert(puzzle)
    z = solve(A, b)
    write_solution(z)

if __name__ == "__main__":
    main()