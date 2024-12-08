#!/usr/bin/env python3

def find_matching(L, pattern):
    repetition = []
    number = 0
    for number, string in enumerate(L):
        print(number)
        print(string)
        if pattern in string:
            repetition.append(number)
    
    print(repetition)
        
    return repetition

def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    pass

if __name__ == "__main__":
    main()
