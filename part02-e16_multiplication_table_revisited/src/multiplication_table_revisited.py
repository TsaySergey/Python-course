#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    arr = np.arange(n)
    row = arr.reshape(1, -1)
    column = arr.reshape(-1, 1)
    print(row)
    print()
    print(column)

    final = row * column
    return final

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
