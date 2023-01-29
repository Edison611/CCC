# CCC '10 J4 - Global Warming

def repeat(years, temps):
    if len(temps) == 1:
        return 0
    cycle = []
    # Check for differences
    for temp in range(len(temps)):
        if temp == years-1:
            break
        dif = temps[temp+1] - temps[temp]
        cycle.append(dif)
    for i in range(len(cycle)):
        cycle[i] = str(cycle[i]) + ","
    cycle = ''.join(cycle)
    #print(cycle)
    # Check for repeating cycle length
    for val in range(1, len(cycle)+1):
        pattern = cycle[:val]
        #print(pattern)
        check = pattern * len(cycle)
        #print(check)
        if cycle in check:
            total = 0
            for string in pattern:
                if string == ",":
                    total += 1
            return total

#print(repeat(6, [1, 3, 6, 8, 11, 16]))
cycles = []
while True:
    inp = input().split()
    for i in range(len(inp)):
        inp[i] = int(inp[i])
    if inp == [0]:
        break
    cycles.append(inp)

for cycle in cycles:
    length = cycle[0]
    cycle.pop(0)
    cyclen = repeat(length, cycle)
    print(cyclen)



