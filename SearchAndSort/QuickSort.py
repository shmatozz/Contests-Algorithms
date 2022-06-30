def quick(left, right):
    global array
    if left < right:
        if left > 0:
            index = (len(array[left:right + 1]) // 2) + left
        else:
            index = len(array[left:right + 1]) // 2
        pivot = array[index]
        print('\nPivot index:', index, ', pivot element:', pivot)
        leftpart = []
        rightpart = []
        pivots = []
        c = index
        for i in range(len(array)):
            if array[i] < pivot:
                leftpart.append(array[i])
                if i > c:
                    index += 1
            if array[i] > pivot:
                if i < c:
                    index -= 1
                rightpart.append(array[i])
            if array[i] == pivot:
                if i > c:
                    index += 1
                elif i < c:
                    index -= 1
                pivots.append(array[i])
        array = leftpart + pivots + rightpart
        print('Array after partition:', *array)
        print(left, c - 1)
        quick(left, c - 1)
        quick(c + 1, right)
        return array
    else:
        return array


n = int(input())
array = list(map(int, input().split()))
print('Initial array:')
print(*array)
quick(0, n - 1)
