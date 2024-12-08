#!/usr/bin/env python3

def extract_numbers(s):
    new_s = s.split()
    final = []
    for word in new_s:
        try:
            value = int(word)
            final.append(value)
        except ValueError:
            try:
                value = float(word)
                final.append(value)
            except ValueError:
                continue


            

    return final

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()
