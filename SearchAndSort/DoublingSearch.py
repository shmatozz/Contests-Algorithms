length, element = map(int, input().split())
array = list(map(int, input().split()))
stepen = -1
end = 0
flag = False
print("Initial array:")
print(*array)
print('Target element:', element)
for i in range(len(array)):
    array[i] = [array[i], i]
history = []
otv = array[:end+1]
while True:
    bounds = []
    if element < otv[-1][0]:
        if otv[-1][1] == end:
            bounds.append(otv[-1][0])
            bounds.append(otv[-1][1])
            history.append(bounds)
        break
    elif element > otv[-1][0]:
        if otv[-1][1] == end:
            bounds.append(otv[-1][0])
            bounds.append(otv[-1][1])
            history.append(bounds)
        stepen += 1
        end = pow(2, stepen)
        if len(otv) == 1 and otv[-1][1] != end // 2 and end != 0:
            flag = True
            history = history[:]
            break
        otv = array[end // 2+1: end+1]
        flag = True
        if len(otv) == 0:
            otv = array[end // 4 + 1:]
            flag = False
            break
    elif element == otv[-1][0]:
        bounds.append(otv[-1][0])
        bounds.append(otv[-1][1])
        history.append(bounds)
        otv = [otv[-1]]
        flag = False
        break
print('Bounds history:', end=' ')
for i in range(len(history)):
    print(history[i][0],'(', history[i][1], ')', sep='', end=' ')
if len(otv) > 0:
    start = otv[0][1]
    finish = otv[-1][1]
history = []
while len(otv) > 0 and array[-1][1] != end // 2:
    avg = (finish - start) // 2
    sravn = []
    if element < otv[avg][0]:
        sravn.append(otv[avg][0])
        sravn.append(otv[avg][1])
        history.append(sravn)
        if len(otv) == 1:
            flag = True
            history = history[:-1]
            break
        finish = otv[avg-1][1]
        otv = otv[:avg]
    elif element == otv[avg][0]:
        sravn.append(otv[avg][0])
        sravn.append(otv[avg][1])
        history.append(sravn)
        otv = otv[avg:avg+1]
        break
    elif element > otv[avg][0]:
        sravn.append(otv[avg][0])
        sravn.append(otv[avg][1])
        history.append(sravn)
        if len(otv) == 1:
            flag = True
            break
        start = otv[avg+1][1]
        otv = otv[avg + 1:]
if flag:
    if len(history) > 0:
        print('\nSearch history:', end=' ')
        for i in range(len(history)):
            print(history[i][0],'(', history[i][1], ')', sep='', end=' ')
if len(otv) > 0 and otv[0][0] == element:
    print('\nTarget is found at:', otv[0][1])
else:
    print('\nNo targets')