#!/usr/bin/env python3
import sys
import re


def file_listing(filename="src/listing.txt"):
    pattern = r"(\d+)\s+(\w{3})\s+(\d{1,2})\s+(\d{1,2}):(\d{2})\s+(.+)"
    file_list = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            match = re.search(pattern, line)
            if match:
                size = int(match.group(1))
                month = (match.group(2))
                day = int(match.group(3))
                hour = int(match.group(4))
                minutes = int(match.group(5))
                name = match.group(6)

                data = (size, month, day, hour, minutes, name)
                file_list.append(data)



        return file_list


def main():
    file_listing()
    pass

if __name__ == "__main__":
    main()
