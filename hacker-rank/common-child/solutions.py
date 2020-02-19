#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.

def commonChild(s1, s2):
    ln = len(s1)
    data = [ [ 0 for i in range(ln+1) ] for i in range(ln+1) ]
    
    for i in range(ln):
        for j in range(ln):
            if s1[i] == s2[j]:
                data[i+1][j+1] =  data[i][j] + 1
            else:
                data[i+1][j+1] = max([data[i+1][j], data[i][j+1]])

    return data[ln][ln]

if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)
    
    print(result)