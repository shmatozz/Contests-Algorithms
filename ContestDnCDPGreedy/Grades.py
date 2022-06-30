n = int(input())
grades = list(map(int, input().split()))
best_len = 0
best_combo = [1]
best_indexes = [-1]
for i in range(1, n):
    current = grades[i]
    best_combo.append(1)
    best_indexes.append(-1)
    for j in range(0, i):
        if grades[j] <= current:
            if best_combo[i] <= best_combo[j]+1:
                best_indexes[i] = j
            best_combo[i] = max(best_combo[i], best_combo[j] + 1)
best_len = max(best_combo)
contenders = []
for i in range(len(best_combo)-1, -1, -1):
    if best_combo[i] == best_len:
        contender = [grades[i]]
        j = best_indexes[i]
        while j != -1:
            contender.insert(0, grades[j])
            j = best_indexes[j]
        contenders.append(contender)
print(contenders)
print('Best length =', best_len)
print('Best combo is: ', *sorted(contenders[0]))
