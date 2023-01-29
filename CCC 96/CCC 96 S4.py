#UNFINISHED
first = int(input())

eq = []
for i in range(first):
    equation = input()
    eq.append(equation)


def convert(num):
    roman = ""



def calc(roman):
    total = 0
    for letter in range(len(roman)):
        if roman[letter] == 'I':
            if letter == len(roman)-1:
                total += 1
                break
            if roman[letter+1] == 'V':
                total += 4
                letter += 1
            elif roman[letter+1] == 'X':
                total += 9
                letter += 1
            else:
                total += 1
        elif roman[letter] == 'V':
            total += 5
        elif roman[letter] == 'X':
            if letter == len(roman)-1:
                total += 10
                break
            if roman[letter+1] == 'L':
                total += 40
                letter += 1
            elif roman[letter+1] == 'C':
                total += 90
                letter += 1
            else:
                total += 10
        elif roman[letter] == 'L':
            total += 50
        elif roman[letter] == 'C':
            if letter == len(roman) - 1:
                total += 100
                break
            if roman[letter + 1] == 'D':
                total += 400
                letter += 1
            elif roman[letter + 1] == 'M':
                total += 900
                letter += 1
            else:
                total += 100
        elif roman[letter] == 'D':
            total += 500
        elif roman[letter] == 'M':
            total += 1000
        else:
            continue
    if total > 1000:
        return "CONCORDIA CUM VERITATE"
    return total


for i in eq:
    print(i + str(calc(i)))