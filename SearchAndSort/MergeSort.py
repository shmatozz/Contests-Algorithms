def merge(left, right):
    slivka = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            slivka.append(left[i])
            i += 1
        else:
            slivka.append(right[j])
            j += 1
    if i == len(left):
        for k in range(j, len(right)):
            slivka.append(right[k])
    elif j == len(right):
        for k in range(i, len(left)):
            slivka.append(left[k])
    return slivka

def sort1(array):
    if len(array) <= 1:
        return array
    left = array[:len(array) // 2]
    right = array[len(array) // 2:]
    sort1(left)
    sort1(right)
    #print("Left part:", *left)
    #print("Right part:", *right)
    slivka = merge(left, right)
    #print('Merged parts:', *slivka, '\n')
    array[:] = slivka[:]
    return array


array = list(map(int, input().split()))
#print('Initial array:')
#print(*array, '\n')
sort1(array)
print(*array)
