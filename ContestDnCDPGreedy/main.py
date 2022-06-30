n, m, l = map(int, input().split())
arrays123 = []
arrays321 = []

for i in range(n):
    arrays123.append(list(map(int, input().split())))
for i in range(m):
    arrays321.append(list(map(int, input().split())))

q = int(input())

for x in range(q):
    i, j = map(int, input().split())
    lower_bound = 0
    higher_bound = l - 1

    min_max = max(arrays123[i - 1][-1], arrays321[j - 1][-1])
    diff = abs(arrays123[i - 1][-1] - arrays321[j - 1][-1])
    while lower_bound < higher_bound:
        mid = (lower_bound + higher_bound) // 2
        mid_max = max(arrays123[i - 1][mid], arrays321[j - 1][mid])
        diff_mid = abs(arrays123[i - 1][mid] - arrays321[j - 1][mid])
        diff_mid1 = abs(arrays123[i - 1][mid + 1] - arrays321[j - 1][mid + 1])
        if mid_max <= min_max and diff_mid <= diff and diff_mid1 >= diff_mid:
            min_max = mid_max
            diff = diff_mid
            higher_bound = mid
        else:
            lower_bound = mid + 1
    print(lower_bound + 1)


