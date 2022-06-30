def k(xy1, xy2):
    if xy1[0] == xy2[0]:
        return 1000000000000000
    else:
        return (xy2[1] - xy1[1]) / (xy2[0] - xy1[0])


def turn(x1, y1, x2, y2, x3, y3):
    if ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) <= 0:
        return 0
    else:
        return 1


file = open('input.txt')
cord = []
for i in file:
    xy = list(map(int, i.split()))
    cord.append(xy)
min1 = min(cord)
cord.remove(min1)
for i in range(1, len(cord)):
    sch = i
    for j in range(i-1, -1, -1):
        if k(min1, cord[sch]) < k(min1, cord[j]):
            x = cord[sch]
            cord[sch] = cord[j]
            cord[j] = x
            sch -= 1
cord.insert(0, min1)
i = 2
while i != len(cord):
    if turn(cord[i-2][0], cord[i-2][1], cord[i-1][0], cord[i-1][1], cord[i][0], cord[i][1]) == 0:
        cord.pop(i-1)
        i -= 1
    else:
        i += 1
cord.sort()
print('Convex Hull is:')
for i in cord:
    print(*i)
