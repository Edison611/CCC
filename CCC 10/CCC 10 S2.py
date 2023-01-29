# CCC '10 S2 - Huffman Encoding

k = int(input())

all = {}

for i in range(k):
    val = input().split()
    all[val[0]] = val[1]

ans = ""

string = input()

while len(string) > 0:
    for thing in all:
        if all[thing] == string[0:len(all[thing])]:
            ans = ans + thing
            string = string[len(all[thing])::]

print(ans)
