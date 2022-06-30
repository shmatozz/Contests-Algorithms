length, element = map(int,input().split())
array = list(map(int, input().split()))
history = []
start = 0
finish = length - 1
otv = []
for i in range(len(array)):
    a = [array[i], i]
    otv.append(a)
while len(otv) != 1:
    avg = (finish - start) // 2
    sravn = []
    if element < otv[avg][0]:
        sravn.append(otv[avg][0])
        sravn.append(otv[avg][1])
        history.append(sravn)
        finish = otv[avg-1][1]
        otv = otv[:avg]
    elif element == otv[avg][0]:
        sravn.append(otv[avg][0])
        sravn.append(otv[avg][1])
        history.append(sravn)
        otv = otv[avg:avg+1]
    elif element > otv[avg][0]:
        sravn.append(otv[avg][0])
        sravn.append(otv[avg][1])
        history.append(sravn)
        start = otv[avg+1][1]
        otv = otv[avg + 1:]
if not (otv[0] in history):
    history.append(otv[0])
print("Initial array:")
print(*array)
print('Target element:', element)
print('Search history:', end=' ')
for i in range(len(history)):
    print(history[i][0],'(', history[i][1], ')', sep='', end=' ')
if otv[0][0] == el:
    print('\nTarget is found at:', otv[-1][1])
else:
    print('\nNo targets')