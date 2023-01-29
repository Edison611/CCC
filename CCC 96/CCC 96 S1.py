# CCC '96 S1 - Deficient, Perfect, and Abundant

n = int(input())
nums = []

for i in range(n):
    k = input()
    nums.append(int(k))

for i in nums:
    s = 0
    for j in range(1,i):
        if i % j == 0:
            s += j
    if s < i:
        print(str(i) + " is a deficient number.")
    if s == i:
        print(str(i) + " is a perfect number.")
    if s > i:
        print(str(i) + " is an abundant number.")