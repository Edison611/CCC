path = [(0,-1),(0,-2),(0,-3),(1,-3),(2,-3),(3,-3),(3,-4),(3,-5),(4,-5),(5,-5),(5,-4),(5,-3),(6,-3),(7,-3),(7,-4),(7,-5),(7,-6),(7,-7),(6,-7),(5,-7),(4,-7),(3,-7),(2,-7),(1,-7),(0,-7),(-1,-7),(-1,-6),(-1,-5)]

for i in range(len(path)):
    path[i] = list(path[i])
pos = [-1,-5]
stop = False
flag = True
while flag:
    com = input().split()
    direction = com[0]
    amount = int(com[1])
    if direction == "q":
        break
    for i in range(amount):
        if direction == "d":
            pos[1] = pos[1]-1
        if direction == "u":
            pos[1] = pos[1]+1
        if direction == "l":
            pos[0] = pos[0]-1
        if direction == "r":
            pos[0] = pos[0]+1
        if pos in path:
            stop = True
        path.append(list(pos))
    if stop == True:
        print(str(pos[0])+" "+str(pos[1])+" DANGER")
        break
    if flag == True:
        print(str(pos[0])+" "+str(pos[1])+" safe")
            
        
