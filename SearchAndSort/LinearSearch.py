n, element = map(int, input().split())
array = list(map(int, input().split()))
found = []
for i in range(len(array)):
    if array[i] == element:
        found.append(i)
print("Initial array:")
print(*array)
print('Target element:', element)
if len(found) > 0:
    print('Target is found at:', *found)
else:
    print('No targets')