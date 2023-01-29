# CCC '10 J2 - Up and Down

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

Nikky = 0
Byron = 0

Ncounter = 0
Bcounter = 0

Ndir = True
Bdir = True

for i in range(s):
    if Ndir == True:
        Ncounter += 1
        Nikky += 1
        if Ncounter == a:
            Ncounter = 0
            Ndir = False
            continue
    if Ndir == False:
        Ncounter += 1
        Nikky -= 1
        if Ncounter == b:
            Ncounter = 0
            Ndir = True
            continue

for i in range(s):
    if Bdir == True:
        Bcounter += 1
        Byron += 1
        if Bcounter == c:
            Bcounter = 0
            Bdir = False
            continue
    if Bdir == False:
        Bcounter += 1
        Byron -= 1
        if Bcounter == d:
            Bcounter = 0
            Bdir = True
            continue
if Byron > Nikky:
    print("Byron")
elif Nikky > Byron:
    print("Nikky")
else:
    print("Tied")

