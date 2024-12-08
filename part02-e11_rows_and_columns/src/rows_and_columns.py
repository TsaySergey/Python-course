#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    all_rows = []
    for i in a:
        all_rows.append(i)
    return all_rows

def get_columns(a):
    all_columns = []
    columns = a.shape[1]
    print(columns)
    for i in range(columns):
        all_columns.append(a[:,i])
    
    return all_columns

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
