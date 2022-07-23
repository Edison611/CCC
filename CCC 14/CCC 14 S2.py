# CCC '14 S2 - Assigning Partners

amount = int(input())

list1 = list(map(str, input().split()))
list2 = list(map(str, input().split()))

pairs = set()

for i in range(amount):
    if list1[i] > list2[i]:
        pairs.add((list1[i],list2[i]))
    else:
        pairs.add((list2[i],list1[i]))


if len(pairs) == int(amount/2):
    print("good")
else:
    print("bad")