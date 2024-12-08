#!/usr/bin/env python3


def main():
    pass
    for i in range(1, 11):
        x = triple(i)
        y = square(i)
        if x < y:
            break
        print(f"triple({i})=={x} square({i})=={y}")



def triple(x):
    return x * 3

def square(x):
    return x ** 2




if __name__ == "__main__":
    main()
