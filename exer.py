#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    agr = {}
    for x in a:
        agr[str(x)] = agr.get(str(x), 0) + 1

    bb = []

    for x, y in agr.items():
        bb.append([int(x), y])

    msx = 0
    tmp = 0
    bb = sorted(bb, key=lambda x: x[0])
    print(bb)
    max_simple = max(bb, key=lambda x: x[1])[1]
    for i in range(1, len(bb)):

        if abs(bb[i - 1][0] - bb[i][0]) <= 1:
            tmp = bb[i - 1][1] + bb[i][1]
            # print(tmp)
            if msx < tmp:
                msx = tmp
    if msx < tmp:
        msx = tmp

    res = msx if msx > max_simple else max_simple
    return res


if __name__ == '__main__':
    fptr = open('input.txt', 'r')
    n = fptr.readline().strip()
    a = list(map(int, fptr.read().split()))
    result = pickingNumbers(a)
    print(result)
    fptr.close()
