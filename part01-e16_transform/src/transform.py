#!/usr/bin/env python3

def transform(s1, s2):
    l1 = list(map(int, s1.split()))
    l2 = list(map(int, s2.split()))
    result = list(map(lambda a_b: a_b[0] * a_b[1], zip(l1,l2)))
    return result

def main():
    transform("1 5 3", "2 6 -1")
    pass

    


if __name__ == "__main__":
    main()
