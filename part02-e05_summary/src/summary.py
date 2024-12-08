#!/usr/bin/env python3

import sys
import math

def summary(filename):

    average = 0.0
    sum_total = 0.0
    temp = 0.0
    sum_all = 0.0
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                continue

    sum_all = sum(numbers)
    
    average = sum_all / len(numbers)

    for number in numbers:
        temp = number - average
        sum_total += pow(temp, 2)
    strdev = math.sqrt(sum_total / (len(numbers) - 1))
        

    


    return (sum_all,average,strdev)

def main():
    for filename in sys.argv[1:]:
        total_sum, average, stddev = summary(filename)
        print(f"File: {filename} Sum: {total_sum:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")

    pass

if __name__ == "__main__":
    main()
