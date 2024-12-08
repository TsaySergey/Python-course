#!/usr/bin/env python3

def distinct_characters(L):
    result = {}
    for string in L: 
        charact = set(string)
        result[string] = len(charact)

    return result

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
