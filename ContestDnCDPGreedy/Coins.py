def print_matrix(array, rows, cols):
    for a in range(rows):
        for b in range(cols):
            if array[a][b] == 1:
                print('(%d,%d)' % (a, b), end=' ')


n, m = map(int, input().split())
matrix = []
coins = []
moves = []
x, y = 0, 0
for i in range(n):
    row = [0] * m
    row2 = [0] * m
    coins.append(row)
    moves.append(row2)
    row = list(input().split())
    if 'S' in row:
        x = i
        y = row.index('S')
    matrix.append(row)
moves[n - 1][m - 1] = 1

for i in range(y + 1, m):
    coins[x][i] = int(matrix[x][i]) + coins[x][i - 1]
for i in range(x + 1, n):
    coins[i][y] = int(matrix[i][y]) + coins[i - 1][y]
for i in range(x + 1, n):
    for j in range(y + 1, m):
        coins[i][j] = max(coins[i - 1][j], coins[i][j - 1]) + int(matrix[i][j])

index = 0
flag_row = 0
flag_col = 0
for i in range(n - 1, x, -1):
    for j in range(m - 1, y, -1):
        if moves[i][j] == 1:
            if coins[i-1][j] >= coins[i][j-1]:
                moves[i-1][j] = 1
                if i - 1 == x:
                    flag_row = 1
                    index = y
            else:
                moves[i][j-1] = 1
                if j - 1 == y:
                    index = x
                    flag_col = 1

print('Path:')
if flag_row:
    while moves[x][index] != 1:
        moves[x][index] = 1
        index += 1
    print_matrix(moves, n, m)
elif flag_col:
    while moves[index][y] != 1:
        moves[index][y] = 1
        index += 1
    print_matrix(moves, n, m)
print('\nCoins: %d' % (coins[n - 1][m - 1]))
for i in range(n):
    for j in range(m):
        print("%4d"%(coins[i][j]), end=' ',)
    print()
for i in range(n):
    for j in range(m):
        print("%4d"%(moves[i][j]), end=' ')
    print()