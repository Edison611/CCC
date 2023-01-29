# CCC '02 S2 - Fraction Action
import math

numerator = int(input())
denominator = int(input())

gcf = 1
if numerator < denominator:
    less = int(numerator)
else:
    less = int(denominator)

for i in range(1, less+1):
    if numerator % i == 0 and denominator % i == 0:
        gcf = i

numerator = int(numerator/gcf)
denominator = int(denominator/gcf)

whole = math.floor(numerator/denominator)
numerator -= whole*denominator
frac = str(numerator) + "/" + str(denominator)

if denominator == 1:
    print(whole)
elif numerator == 0:
    print(0)
elif whole == 0:
    print(frac)
else:
    print(str(whole) + " " + frac)

