# CCC '10 S1 - Computer Purchase

n = int(input())
all = {}
for comp in range(n):
    inp = input().split()
    total = 2*int(inp[1])+3*int(inp[2])+int(inp[3])
    all[inp[0]] = total

ans = ""
for i in range(2):
    best = 0
    if n == 0:
        break
    for key in all:
        if all[key] > best:
            best = all[key]
            ans = key
        if all[key] == best:
            li = [ans, key]
            sort = sorted(li)
            ans = sort[0]
    print(ans)
    del all[ans]
    if len(all) == 0:
        break