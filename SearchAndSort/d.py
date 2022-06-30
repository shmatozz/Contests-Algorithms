def quicksort(array, start, end):
    if start < end:
        index, array = partition(array, start, end)
        print(array)
        print(index)
        quicksort(array, start, index - 1)
        print(index, 'e')
        quicksort(array, index + 1, end)

def partition(array, left, right):
    print(left,right)
    pivot = array[(right - left) // 2]
    index = 0
    leftpart = []
    rightpart = []
    pivots = []
    for i in range(len(array)):
        if array[i] < pivot:
            leftpart.append(array[i])
            index += 1
        if array[i] > pivot:
            rightpart.append(array[i])
        if array[i] == pivot:
            pivots.append(array[i])
    array = leftpart + pivots + rightpart
    if len(leftpart) == 0:
        index = len(pivots)
    print(leftpart, pivots, rightpart)
    return index, array


n = int(input())
array = list(map(int, input().split()))
quicksort(array, 0, n-1)
