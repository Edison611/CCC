# CCC '14 J2 - Vote Count

amount = int(input())
winners = input()

counter = 0
counterb = 0

for char in winners:
    if char == "A":
        counter += 1
    if char == "B":
        counterb += 1

if counterb == counter:
    print("Tie")
elif counterb <= counter:
    print("A")
else:
    print("B")