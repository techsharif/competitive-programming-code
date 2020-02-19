#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    row = len(matrix)
    collumn = len(matrix[0])

    total_lines = min(row, collumn) // 2

    lines = [[] for i in range(total_lines)]
    new_matrix = [ [] for i in range(row) ] 
    for rr in range(row):
        for c in range(collumn):
            new_matrix[rr] += [0]
    

    for line in range(total_lines):
        for i in range(line, collumn-line):
            lines[line] += [matrix[line][i]]
        for i in range(line+1, row-line):
            lines[line] += [matrix[i][collumn-line-1]]
        for i in range(collumn-line-2, line, -1):
            lines[line] += [matrix[row-line-1][i]]
        for i in range(row-line-1, line, -1):
            lines[line] += [matrix[i][line]]

    for i in range(total_lines):
        ln = len(lines[i])
        offset = r % ln
        lines[i] = lines[i][offset:] + lines[i][:offset]

    for line in range(total_lines):
        index = 0
        for i in range(line, collumn-line):
            new_matrix[line][i] = lines[line][index]
            index += 1
        for i in range(line+1, row-line):
            new_matrix[i][collumn-line-1] = lines[line][index]
            index += 1
        for i in range(collumn-line-2, line, -1):
            new_matrix[row-line-1][i] = lines[line][index]
            index += 1
        for i in range(row-line-1, line, -1):
            new_matrix[i][line] = lines[line][index]
            index += 1
    
    for i in range(row):
        print(" ".join(list(map(str, new_matrix[i]))))

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
