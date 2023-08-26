# Day 7 of Hackerrank 30 days of code 
#printing an array elements in reverse order seperated by a spaces
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    rarr=arr[::-1] #reads array into new array in reverse order [::-1] will basically reverse(iterate from last) the elements in the list.
print(*rarr) # * will print space seperated  list of the elements
