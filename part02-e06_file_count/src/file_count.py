#!/usr/bin/env python3

import sys

def file_count(filename):
    file_lines = 0
    file_words = 0
    file_characters = 0

    with open(filename, 'r') as file:
        lines = file.readlines()
        file_lines = len(lines)
        file_words = sum(len(line.split()) for line in lines)
        file_characters = sum(len(line) for line in lines)
    


        
        

    
    return (file_lines, file_words, file_characters)

def main():
    filename = 'src/test.txt'
    for filename in sys.argv[1:]:
        file_lines, file_words, file_characters = file_count(filename)
        print(f"{file_lines}\t{file_words}\t{file_characters}\t{filename}")
    pass

if __name__ == "__main__":
    main()
