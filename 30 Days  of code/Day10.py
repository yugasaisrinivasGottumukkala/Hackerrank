#Day 10 Of Hackerrank #0 days of code
#Binary numbers
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    n1=str(bin(n)).strip("0b")
    count=0
    number_of_ones=0
    for i in n1:
        if i=='1':
            number_of_ones+=1
            max_c=max(number_of_ones,count)
        else:
            count=max(number_of_ones,count)
            number_of_ones=0
    print(max_c)
