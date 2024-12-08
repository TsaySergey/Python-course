#!/usr/bin/env python3

def interleave(*lists):
    kek = list(zip(*lists))
    kek = [item for sublist in kek for item in sublist]
    return kek

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
