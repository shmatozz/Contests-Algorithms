def priora(symbol):
    priori = None
    if symbol in '+-':
        priori = 1
    elif symbol in '*/':
        priori = 2
    elif symbol in '(':
        priori = -1
    return priori


n = input()
print('Expression:')
print(n)
array = []
refill = ''
for i in range(len(n)):
    if n[i].isdigit():
        refill += n[i]
    elif n[i] in '(':
        array.append(n[i])
        refill = ''
    elif n[i] in ')':
        array.append(int(refill))
        refill = ''
        array.append(n[i])
    else:
        if len(refill) > 0:
            array.append(int(refill))
        array.append(n[i])
        refill = ''
if len(refill) > 0:
    array.append(refill)
stack = [0]
index = 0
opz = ''
for i in range(len(array)):
    if str(array[i]).isdigit():
        opz += str(array[i]) + ' '
    else:
        if index == 0 or array[i] in '(':
            stack.append(array[i])
            index += 1
        elif array[i] == ')':
            while stack[index] != '(':
                opz += stack[index] + ' '
                stack = stack[:-1]
                index -= 1
            stack = stack[:-1]
            index -= 1
        elif priora(array[i]) < priora(stack[index]):
            while stack[index] == '+' or stack[index] == '-' or stack[index] == '*' or stack[index] == '/':
                opz += stack[index] + ' '
                index -= 1
            index += 1
            stack[index] = array[i]
        elif priora(array[i]) == priora(stack[index]):
            opz += stack[index] + ' '
            stack[index] = array[i]
        elif priora(array[i]) > priora(stack[index]):
            stack.append(array[i])
            index += 1
while index != 0:
    opz += stack[index] + ' '
    index -= 1
print('Reverse Polish Notation:')
print(opz)
opz = list(opz.split())
calculate = []
for i in range(len(opz)):
    if opz[i].isdigit():
        calculate.append(int(opz[i]))
    elif opz[i] == '+':
        calculate[-2] = calculate[-2] + calculate[-1]
        calculate = calculate[:-1]
    elif opz[i] == '-':
        calculate[-2] = calculate[-2] - calculate[-1]
        calculate = calculate[:-1]
    elif opz[i] == '*':
        calculate[-2] = calculate[-2] * calculate[-1]
        calculate = calculate[:-1]
    elif opz[i] == '/':
        calculate[-2] = int(calculate[-2] / calculate[-1])
        calculate = calculate[:-1]
print('Result:')
print(*calculate)