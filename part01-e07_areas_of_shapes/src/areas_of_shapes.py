#!/usr/bin/env python3

import math


def main():
    while 1 == 1:
        shape=input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        elif shape == "triangle": 
            triangle()
        elif shape == "rectangle":
            rectangle()
        elif shape == "circle":
            circle()
        else: print("Unknown shape!")
        

def triangle():
    x = float(input("Give base of the triangle: "))
    y = float(input("Give height of the triangle: "))
    
    area = (y * x) // 2
    print(f"The area is {area}")

def rectangle():
    x = float(input("Give width of the rectangle: "))
    y = float(input("Give height of the rectangle: "))
    area = x * y
    print(f"The area is {area}")

def circle():
    x = float(input("Give radius of the circle: "))
    area = math.pi * x**2
    print(f"The area is {area}")

    
if __name__ == "__main__":
    main()
