#!/usr/bin/env python3

# Created By: Nicolas Riscalas

# Date: Febuary, 23, 2022

# This program calculates the area and perimeter of a rectangle.


def main():
    l = int(input("Length : "))
    w = int(input("Width : "))
    area = l * w
    perimeter = 2 * (l + w)
    print("Area of Rectangle : ", area)
    print("Perimeter of Rectangle : ", perimeter)


if __name__ == "__main__":
    main()
