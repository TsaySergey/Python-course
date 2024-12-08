#!/usr/bin/env python3

def reverse_dictionary(d):
    result = {}
    
    for eng_word, fin_words in d.items(): 
        for fin_word in fin_words:
            if fin_word in result:
                result[fin_word].append(eng_word)
            else:
                result[fin_word] = [eng_word]
    
        
    return result

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))
    pass
    

if __name__ == "__main__":
    main()
