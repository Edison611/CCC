# CCC '12 S3 - Absolutely Acidic
from itertools import combinations

inp = int(input())

frequencies = {}

for i in range(inp):
    sensor = int(input())
    if sensor not in frequencies:
        frequencies[sensor] = 1
    else:
        frequencies[sensor] = frequencies[sensor] + 1

largest = max(frequencies.values())

first = []
second = []

for key in frequencies:
    if frequencies[key] == largest:
        first.append(key)

greatest = 0
if len(first) > 1:
    comb = list(combinations(first, 2))
    for i in comb:
        if abs(i[0]-i[1]) > greatest:
            greatest = abs(i[0]-i[1])

    print(greatest)
else:
    for i in first:
        if i in frequencies:
            frequencies.pop(i)
    largest = max(frequencies.values())
    for key in frequencies:
        if frequencies[key] == largest:
            second.append(key)
    if len(second) > 1:
        for i in second:
            if abs(first[0]-i) > greatest:
                greatest = abs(first[0]-i)
    else:
        greatest = abs(first[0]-second[0])
    print(greatest)


