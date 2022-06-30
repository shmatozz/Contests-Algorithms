n = int(input())
array = []
for i in range(1,n + 1):
    if i % 2 == 0:
        array.append(i)
for i in range(n, 0, -1):
    if i % 2 != 0:
        array.append(i)
print(*array)