"""
Write a function named as logFunc which accept an integer X, Inside function use math.log function to
 calculate log of given number X and return log value. X should be integer, So write a validation function
 inside logFunc to validate if X is an integer or not. If X is not passed, the function should return value
 of math.log(10). See Tutorial
"""
import math
def logFunc(x=10):
    return math.log(x)

print("if u dont want to give an input means click -1")
print("enter your input")

x=int(input())

if x==-1:
    print(logFunc())
else:
    print(logFunc(x))