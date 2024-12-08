#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    
    with open(filename, 'r') as file:
        lines = file.readlines()

    final_list = []
    pattern = "(\d+)\s+(\d+)\s+(\d+)\s+(.+)"

    for line in lines:
        match = re.search(pattern, line.strip())
        if match:
            first_number = match.group(1)
            second_number = match.group(2)
            third_number = match.group(3)
            text = match.group(4)
            cleaned_line = f"{first_number}\t{second_number}\t{third_number}\t{text}"
            final_list.append(cleaned_line)

    return final_list


def main():
    print(red_green_blue())
    pass

if __name__ == "__main__":
    main()
