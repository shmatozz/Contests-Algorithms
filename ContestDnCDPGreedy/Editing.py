main_string = input()
len_ms = len(main_string)
n = int(input())
counts = []
words = []
for k in range(n):
    word = input()
    len_word = len(word)
    operations = []
    for i in range(len_ms + 1):
        a = [0] * (len_word + 1)
        operations.append(a)
    for i in range(len_ms + 1):
        operations[i][0] = i
    for i in range(len_word + 1):
        operations[0][i] = i
    for i in range(1, len_ms + 1):
        for j in range(1, len_word + 1):
            if main_string[i - 1] == word[j - 1]:
                equal = 0
            else:
                equal = 1
            operations[i][j] = min(operations[i-1][j] + 1, operations[i][j-1] + 1, operations[i-1][j-1] + equal)
    counts.append(operations[-1][-1])
    words.append(word)
min_count = min(counts)
print('Most similar words =', counts.count(min_count))
print('Minimal operations needed =', min_count)
for i in range(n):
    if counts[i] == min_count:
        print(words[i])
