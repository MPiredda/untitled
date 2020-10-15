import math
import sys

def factorial(n):
    return math.factorial(n)

if (__name__ == "__main__"):
    print("Run as stand alon script")
    if len(sys.argv) > 1:
        print(factorial(int(sys.argv[1])))
    else:
        print(" I am a module ")