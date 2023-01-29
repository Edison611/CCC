# CCC '02 S1 - The Students' Council Breakfast

PINK = int(input())
GREEN = int(input())
RED = int(input())
ORANGE = int(input())
total = int(input())

ans = 0
minim = total

for i in range(total+1):
 for j in range(total+1):
  for k in range(total+1):
   for l in range(total+1):
    t = 0
    amount = i*PINK + j*GREEN + k*RED + l*ORANGE
    if amount == total:
     if minim > (i+j+k+l):
      minim = i+j+k+l
     print("# of PINK is " + str(i) + " # of GREEN is " + str(j) + " # of RED is " + str(k) + " # of ORANGE is " + str(l))
     ans += 1

print("Total combinations is " + str(ans) + ".")
print("Minimum number of tickets to print is " + str(minim) + ".")

