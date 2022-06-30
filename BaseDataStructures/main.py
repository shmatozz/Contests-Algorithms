t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    max_min = min(array)
    while len(array) > 0:
        array.sort()
        local_min = array[0]
        if local_min > max_min:
            max_min = local_min
        array.pop(0)
        n -= 1
        array = [x - 1 for x in array]
    print(max_min)
