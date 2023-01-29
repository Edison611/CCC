# CCC '12 S4 - A Coin Game
import sys
import copy

path = []

sys.setrecursionlimit(2000)


def recur(pos):
    queue = [(pos, 0)]
    visited = []
    end = [[100, i] for i in range(1, 1+len(pos))]

    while len(queue) != 0:
        current_pos = queue[0][0]
        current_moves = queue[0][1]
        queue.pop(0)
        if current_pos == end:
            return current_moves
            break
        if current_pos in visited:
            continue
        visited.append(current_pos)

        # Finding neighbouring moves
        for i in range(len(pos)):
            new_pos = copy.deepcopy(current_pos)
            if i == len(current_pos)-1:
                if current_pos[i][-1] < current_pos[i - 1][-1]:
                    new_pos[i - 1].append(new_pos[i][-1])
                    new_pos[i].pop(-1)
                    queue.append((new_pos, current_moves+1))
                continue

            if current_pos[i][-1] < current_pos[i+1][-1]:
                new_pos[i + 1].append(new_pos[i][-1])
                new_pos[i].pop(-1)
                queue.append((new_pos, current_moves+1))
                new_pos = copy.deepcopy(current_pos)
            if i == 0:
                continue

            if current_pos[i][-1] < current_pos[i-1][-1]:
                new_pos[i - 1].append(new_pos[i][-1])
                new_pos[i].pop(-1)
                queue.append((new_pos, current_moves+1))
    return "IMPOSSIBLE"


while True:
    n = int(input())
    if n == 0:
        break
    orientation = list(map(int, list(input().split())))
    for i in range(len(orientation)):
        orientation[i] = [100, orientation[i]]

    print(recur(orientation))





