#!/bin/python3

import math
import os
import random
import re
import sys
import time


def bin_found(a, b, arr, x):
    if a == b:
        if a == 0 and x >= arr[0]:
            return a + 1
        return a + 2
    else:
        k = 0 if (b - a) % 2 == 0 else 1
        m = a + (b - a + k) // 2

        if x < arr[m]:
            return bin_found(m, b, arr, x)
        elif x > arr[m]:
            return bin_found(a, m-1, arr, x)
        else:
            return m + 1


# dComplete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    res = []
    agr_score = []
    for i in range(0, len(scores) - 1):
        if scores[i] != scores[i + 1]:
            agr_score.append(scores[i])
    if len(scores) == 2 and scores[-2] != scores[-1]:
        agr_score.append(scores[-1])
    else:
        agr_score.append(scores[-1])

    for ali_sc in alice:
        position = bin_found(0, len(agr_score)-1, agr_score, ali_sc)
        res.append(position)
    return res


if __name__ == '__main__':
    fptr = open('input.txt', 'r')

    scores_count = int(fptr.readline())
    scores = list(map(int, fptr.readline().rstrip().split()))

    alice_count = int(fptr.readline())
    alice = list(map(int, fptr.readline().rstrip().split()))

    t = time.time()
    result = climbingLeaderboard(scores, alice)
    print(time.time() - t)
    fptr.close()
