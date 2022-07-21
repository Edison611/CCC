year = int(input())

while year > -1:
    year += 1
    Y = list(str(year))
    if len(Y) == len(set(Y)):
        print(year)
        break
        
