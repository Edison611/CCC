# CCC '10 S4 - Animal Farm

M = int(input())

repeat = []
pen = {}
cost = {}

for i in range(M):
    p = input().split()
    fence = list(map(int, list(p[1:int(p[0]) + 1])))
    costs = list(map(int, list(p[int(p[0]) + 1::])))
    for j in range(len(fence)):
        if j == len(fence) - 1:
            segment = [fence[0], fence[-1]]
        else:
            segment = [fence[j], fence[j + 1]]
        if segment[0] > segment[1]:
            segment.reverse()
        segment = tuple(segment)
        if i + 1 in pen:
            pen[i + 1].append(segment)
        else:
            pen[i + 1] = [segment]
        if segment in cost:
            repeat.append(segment)
        cost[segment] = costs[j]

visited = [(1, 2)]
queue = [pen[1][0]]
solutions = []
print(pen)
print(cost)

#def prim():
    #for i in pen:

'''
def bfs(current):
    #print("current: ", current)
    #print("visited: ", visited)

    outside = {}
    for i in range(M):
        outside[i + 1] = set()
    status = set()
    for fence in current:
        for key in pen:
            for value in pen[key]:
                if value == fence:
                    if fence not in repeat:
                        outside[key].append(0)
                    else:
                        status.add(key)

    if len(current) == 3:
        # print("solutions: ", solutions)
        solutions.append(set(current))
        visited.pop(-1)
        current.pop(-1)
        return

    neighbours = []

    for shape in pen:
        if current[-1] in pen[shape]:
            for i in pen[shape]:
                if i not in visited and i == min(pen[shape]):
                    neighbours.append(i)

    #print("neighbours: ", neighbours)
    if len(neighbours) == 0:
        visited.pop(-1)
        current.pop(-1)
        return

    for neighbour in neighbours:
        if neighbour not in visited:
            visited.append(neighbour)
            current.append(neighbour)
            bfs(current)
    current.pop(-1)


for line in cost:
    bfs([line])

print(len(solutions))
'''
# print(queue)
# print(pen)
# print(cost)
# print(status)
'''
visited = []
queue = [1]
lowest = pen[1][0]
for fence in pen[1]:
    if cost[fence] < lowest:
        lowest = fence
queue = lowest
while True:
    lowest = pen[current][0]
    for fence in pen[current]:
        if cost[fence] < lowest:
            lowest = fence
    visited.append(lowest)
    neighbours = []
    for shape in pen:
        if lowest in pen[shape]:
            for i in pen[shape]:
                if i not in visited:
                    neighbours.append(i)

'''