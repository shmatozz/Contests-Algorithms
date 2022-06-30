def minimum(array, used_min):
    min1 = max(array)
    index = array.index(max(array))
    for a in range(len(array)):
        if array[a] < min1 and used_min[a] != -1 and array[a] != 0:
            min1 = array[a]
            index = a
    if used_min[index] == -1:
        min1 = -1
    return min1, index


def min_cost(table, start, k):
    cost, count = 0, 1
    used = [0] * k
    roads = []
    no_way = 0
    while count != k:
        roads.append(start)
        used[start] = -1
        buffer = table[start]
        min_buffer, ind = minimum(buffer, used)
        if min_buffer != -1:
            cost += min_buffer
            start = ind
        else:
            no_way = 1
        count += 1
    roads.append(start)
    return cost, start, roads, no_way


n = int(input())
matrix = []
costs = []
all_ways = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n):
    cost, end, ways, flag_no_way = min_cost(matrix, i, n)
    if flag_no_way == 0 and matrix[end][i] != 0:
        cost += matrix[end][i]
        costs.append(cost)
        ways.append(i)
        all_ways.append(ways)
if len(costs) > 0:
    print('Path:')
    print(*all_ways[costs.index(min(costs))])
    print('Cost:', min(costs))
else:
    print('Lost')
