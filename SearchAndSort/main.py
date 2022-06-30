n = int(input())
count = 0
array = list(map(int, input().split()))
while len(array) >= 1:
    count += array.index(min(array))
    array.pop(array.index(min(array)))
print(count)
