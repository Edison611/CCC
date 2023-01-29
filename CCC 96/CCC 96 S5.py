# CCC '96 S5 - Maximum Distance

first = int(input())


def distance(X, Y):
    maximum = 0
    pos = {}
    for i in range(len(X)):
        if X[i] in pos:
            continue
        pos[X[i]] = i
    for i in range(len(Y)):
        if Y[i] not in pos:
            continue
        if i-pos[Y[i]] > maximum:
            maximum = i-pos[Y[i]]
    return maximum


lists = []
for i in range(first):
    num = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    lists.append((X, Y))

for i in lists:
    print("The maximum distance is " + str(distance(i[0], i[1])))