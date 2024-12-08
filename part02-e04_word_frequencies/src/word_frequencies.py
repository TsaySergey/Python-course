#!/usr/bin/env python3
import re

def word_frequencies(filename):
    word_count = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
    
        for line in lines:
            words = line.split()

            for word in words:
                cleaned_word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                
                if cleaned_word:
                    if cleaned_word in word_count:
                        word_count[cleaned_word] += 1
                    else:
                        word_count[cleaned_word] = 1
        

    return word_count

def main():
    filename = 'src/alice.txt'
    frequencies = word_frequencies(filename)
    
    for word, count in frequencies.items():
        print(f"{word}\t{count}")
    pass

if __name__ == "__main__":
    main()
