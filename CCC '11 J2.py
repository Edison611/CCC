h = int(input())
M = int(input())

t = 0
while t < M:
    t += 1
    if ((-6*t**4)+(h*t**3)+(2*t**2)+t) <= 0:
        print("The balloon first touches ground at hour:")
        print(str(t))
        break
    if t == M:
        print("The balloon does not touch ground in the given time.")
