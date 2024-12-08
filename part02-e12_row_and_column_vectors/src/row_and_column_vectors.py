#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    output = []
    for i in a:
        reshaped_row = i.reshape(1,-1)
        output.append(reshaped_row)

    return output

def get_column_vectors(a):
    column = a.shape[1]
    output = []
    
    for i in range(column):
        output.append(a[:,i:i+1])
       
    return output

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
