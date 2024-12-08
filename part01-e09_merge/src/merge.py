#!/usr/bin/env python3

def merge(L1, L2):
    L = L1 + L2
    x = len(L)
    for i in range(x):
        for j in range(0, x - i - 1):
            if L[j] > L[j+1]: 
                L[j], L[j+1] = L[j+1], L[j]            

    return L

def main():
    pass


if __name__ == "__main__":
    main()
