#!/usr/bin/env python3

# Created By: Nicolas Riscalas

# Date: February 18 2022

# Basic math program

numbers = list(map(int, input("Input 2 numbers\n").strip().split()))

numAdd = numbers[0] + numbers[1]
numSub = numbers[0] - numbers[1]
numDiv = numbers[0] / numbers[1]
numMult = numbers[0] * numbers[1]
numPow = numbers[0] ** numbers[1]
numRoot = (numbers[0] ** 1./numbers[1])

print("the numbers added is {}\n".format(numAdd))
print("The numbers subtracted is {}\n".format(numSub))
print("The numbers multiplied is {}\n".format(numMult))
print("The numbers divided is {}\n".format(numDiv))
print("Number 1 to the power of number 2 is {}\n".format(numPow))
print("Number 2 to the root of number 1 is {}\n".format(numRoot))
