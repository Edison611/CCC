# CCC '97 S2 - Nasty Numbers

import math


def factor(num):
    factors = []
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            other = int(num/i)
            factors.append((i, other))
    return factors


first = int(input())

all = []
for i in range(first):
    num = int(input())
    all.append(num)

for num in all:
    sums = []
    difs = []
    factors = factor(num)

