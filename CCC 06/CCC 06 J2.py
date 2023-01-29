#CCC '06 J2 - Roll the Dice

n = int(input())
m = int(input())

total = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        if i + j == 10:
            total += 1

if total == 1:
    print("There is 1 way to get the sum 10.")
else:
    print("There are " + str(total) + " ways to get the sum 10.")