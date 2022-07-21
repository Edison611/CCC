word = input()

allowed = ["I", "O", "S", "H", "Z", "X", "N"]

counter = 0
for letter in word:
    if letter not in allowed:
        print("NO")
        counter += 1
        break
if counter == 0:
    print("YES")
