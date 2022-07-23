# CCC '14 J3 - Double Dice

amount = int(input())

David = 100
Anna = 100

for i in range(amount):
    rolls = list(map(int, input().split()))
    if rolls[0] == rolls[1]:
        continue
    elif rolls[0] > rolls[1]:
        David -= rolls[0]
    else:
        Anna -= rolls[1]
print(Anna)
print(David)
