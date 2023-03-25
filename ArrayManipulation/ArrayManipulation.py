#!/bin/python3
#Problem Statement: 
#https://www.hackerrank.com/challenges/crush/problem

import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
    arr = [0]*n
    maxx = adder = 0
    for query in queries:
        arr[query[0]-1] += query[2]
        if( query[1] < n):
            arr[query[1]] -= query[2]
    for i in arr:
        adder += i
        maxx = max(maxx,adder)

    return maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
