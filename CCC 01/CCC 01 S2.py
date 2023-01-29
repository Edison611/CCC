# CCC '01 S2 - Spirals

start = int(input())
end = int(input())


class Dir:

    def __init__(self, num):
        self.spiral = [[num]]
        self.current = 0
    
    def down(self, num):
        if self.current == len(self.spiral) - 1:
            self.spiral.append([num])
            self.current += 1
        else:
            self.current += 1
            self.spiral[self.current].insert(0, num)

    def right(self, num):
        self.spiral[-1].append(num)

    def up(self, num):
        if self.current == 0:
            self.spiral.insert(0, [num])
        else:
            self.spiral[self.current - 1].append(num)
            self.current -= 1

    def left(self, num):
        self.spiral[0].insert(0, num)

    def string(self):
        final = ""
        longest = len(self.spiral[0])
        for row in self.spiral:

            if len(row) == longest:
                final = final + " ".join(list(map(str, row))) + " \n"
            else:
                final = final + " ".join(list(map(str, row))) + " \n"
        return final


direction = ["down", "right", "up", "left"]

spiral = Dir(start)

final = ""
count = 1
while start <= end:
    if start == end:
        final = start
        break
    for i in range(count):
        start += 1
        if count % 2 == 1:
            spiral.down(start)
        else:
            spiral.up(start)
        if start >= end:
            final = str(spiral.string())
            break
    if start >= end:
        final = str(spiral.string())
        break
    for i in range(count):
        start += 1
        if count % 2 == 1:
            spiral.right(start)
        else:
            spiral.left(start)
        if start >= end:
            final = str(spiral.string())
            break
    if start >= end:
        final = str(spiral.string())
        break
    count += 1

print(final)