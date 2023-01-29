# CCC '12 S1 - Don't pass me the ball!

import math

num = int(input())

if num < 4:
    print(0)
else:
    print(int((math.factorial(num-1))/(6*(math.factorial(num-4)))))
