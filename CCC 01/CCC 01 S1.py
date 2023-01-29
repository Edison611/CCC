cards = input()

total = 0
pointlist = {"J":1, "Q":2, "K":3, "A":4}
suits = {"C":[], "D":[], "H":[], "S":[]}
words = {"C":"Clubs", "D":"Diamonds", "H":"Hearts", "S":"Spades"}
for card in cards:
    if card in suits:
        suit = card
        continue
    suits[suit].append(card)

total = 0
print("Cards Dealt              Points")
for suit in suits:
    points = 0
    if len(suits[suit]) == 0:
        points += 3
    if len(suits[suit]) == 1:
        points += 2
    if len(suits[suit]) == 2:
        points += 1
    for letter in suits[suit]:
        if letter not in pointlist:
            continue
        points += pointlist[letter]
    total += points
    print(words[suit] + " " + " ".join(suits[suit]) + "               " + str(points))
print("Total " + str(total))