#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    sort_arr = arr[:]
    sort_arr.sort()

    min_ = -1
    max_ = -1

    total = 0

    ln = len(arr)

    for i in range(ln):
        if arr[i] != sort_arr[i]:
            total += 1
            if min_ == -1:
                min_ = i
            else:
                max_ = i
    

    if total == 0:
        print("yes")
    elif total == 2:
        print("yes")
        print("swap {} {}".format(min_+1, max_+1))
    elif total // 2 == (max_ - min_ + 1) // 2:
        flag = True
        for i in range(max_ - min_ + 1):
            arr_index = min_ + i
            sort_index = max_ - i

            if (arr[arr_index] != sort_arr[sort_index]):
                    flag = False

        if flag:
            print("yes")
            print("reverse {} {}".format(min_+1, max_+1))
        else:
            print("no")
    else:
        print("no")
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
