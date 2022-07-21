time = int(input())
C = int(input())

chores = []
for i in range(C):
    chore = int(input())
    chores.append(chore)

chores = sorted(chores)

total = 0
choretime = 0
for num in chores:
    if choretime == time:
        print(total)
        break
    if choretime > time:
        print(total-1)
        break
    choretime += num
    total += 1
