# 	CCC '96 S2 - Divisibility by 11

n = int(input())

nums = []

for i in range(n):
    num = input()
    nums.append(num)

for num in nums:
    begin = num
    for i in range(len(num)):
        print(num)
        last = int(num[-1])
        num = str(int(num[:-1])-last)
        if int(num) == 11:
            print("The number " + str(begin) + " is divisible by 11.")
            break
        if int(num) < 11:
            print("The number " + str(begin) + " is not divisible by 11.")
            break

