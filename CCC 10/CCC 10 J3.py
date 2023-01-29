# CCC '10 J3 - Punchy

import math


class Operations:

    def __init__(self, value):
        self.value = value

    def out(self):
        print(self.value)

    def add(self, var1, var2):
        self.value = var1 + var2

    def mul(self, var1, var2):
        self.value = var1 * var2

    def sub(self, var1, var2):
        self.value = var1 - var2

    def div(self, var1, var2):
        self.value = math.trunc(var1 / var2)


letter = {}

A = Operations(0)
B = Operations(0)
while True:
    letter["A"] = A
    letter["B"] = B
    inp = input().split()
    if inp[0] == "1":
        if inp[1] == "A":
            A = Operations(int(inp[2]))
            letter["A"] = A
        else:
            B = Operations(int(inp[2]))
            letter["B"] = B
    elif inp[0] == "2":
        if inp[1] == "A":
            print(A.value)
        else:
            print(B.value)
    elif inp[0] == "3":
        letter[inp[1]].add(letter[inp[1]].value, letter[inp[2]].value)
    elif inp[0] == "4":
        letter[inp[1]].mul(letter[inp[1]].value, letter[inp[2]].value)
    elif inp[0] == "5":
        letter[inp[1]].sub(letter[inp[1]].value, letter[inp[2]].value)
    elif inp[0] == "6":
        letter[inp[1]].div(letter[inp[1]].value, letter[inp[2]].value)
    else:
        break
