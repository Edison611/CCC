D11 = input()
D12 = input()
D13 = input()

num = "9780921418"
num = num+D11+D12+D13

total = 0
for i in range(1,len(num)+1):
    if i % 2 == 0:
        total += int(num[i-1])*3
    else:
        total += int(num[i-1])

print(total)
