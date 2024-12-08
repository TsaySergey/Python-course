#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    discrimintant = b*b - 4*a*c
    
    x1 = (-b + math.sqrt(discrimintant)) / (2 * a)
    x2 = (-b - math.sqrt(discrimintant)) / (2 * a)
    return (x1,x2)


def main():
    pass
    


if __name__ == "__main__":
    main()
