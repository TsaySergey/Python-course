#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return '0 = 0'
    numbers_str = ' + '.join(map(str, L))
    total_sum = sum(L)
    final_equation = f'{numbers_str} = {total_sum}'
    return f"{final_equation}"

def main():
    print(sum_equation([1,5,7]))
    pass

if __name__ == "__main__":
    main()
