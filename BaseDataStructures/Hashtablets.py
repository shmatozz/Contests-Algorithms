def hash_function(hash, q, p):
    sum1 = 0
    n = len(hash)
    for i in range(len(hash)):
        sum1 += ((ord(hash[i])) - 96) * (p**(i))
    sum1 = sum1 % q
    return sum1


def put(index, key, value):
    global ArrayOfValues, ArrayOfKeys, HistoryArray
    if ArrayOfValues[index] is None or ArrayOfKeys[index] == key or ArrayOfKeys[index] == 'was used':
        ArrayOfKeys[index] = key
        ArrayOfValues[index] = value
        result_put = 'inserted'
        linear_probing = 0
        HistoryArray[index] = 0
    else:
        result_put = 'collision'
        linear_probing = None
        for i in range(index + 1, len(ArrayOfValues)):
            if ArrayOfValues[i] is None:
                ArrayOfKeys[i] = key
                ArrayOfValues[i] = value
                linear_probing = i
                HistoryArray[i] = 0
                break
        if linear_probing is None:
            for i in range(0, index + 1):
                if ArrayOfValues[i] is None:
                    ArrayOfKeys[i] = key
                    ArrayOfValues[i] = value
                    linear_probing = i
                    HistoryArray[i] = 0
                    break
                if i == index:
                    result_put = 'overflow'
    return result_put, linear_probing


def get(index, key):
    global ArrayOfValues, HistoryArray, ArrayOfKeys
    result_get = 'no_key'
    linear_probing = None
    value_get = 'no_key'
    if ArrayOfKeys[index] == key:
        result_get = 'found'
        value_get = ArrayOfValues[index]
        linear_probing = index
    elif ArrayOfKeys[index] is None:
        value_get = 'no_key'
        result_get = 'no_key'
    elif ArrayOfKeys[index] != key:
        result_get = 'collision'
        linear_probing = None
        for i in range(index, len(ArrayOfKeys)):
            if ArrayOfKeys[i] == key:
                value_get = ArrayOfValues[i]
                linear_probing = i
                break
            elif HistoryArray[i] == -1:
                linear_probing = i
                break
        if linear_probing is None:
            for i in range(0, index):
                if ArrayOfKeys[i] == key:
                    value_get = ArrayOfValues[i]
                    linear_probing = i
                    break
                elif HistoryArray[i] == -1:
                    linear_probing = i
                    break
    return result_get, linear_probing, value_get


def delete(index, key):
    global ArrayOfValues, ArrayOfKeys, HistoryArray
    result_del = 'no_key'
    linear_probing = 0
    value_del = 'no_key'
    if ArrayOfKeys[index] == key:
        result_del = 'removed'
        value_del = ArrayOfValues[index]
        ArrayOfKeys[index] = 'was used'
        ArrayOfValues[index] = 'was used'
        HistoryArray[index] = 1
        linear_probing = index
    elif ArrayOfKeys[index] is None:
        result_del = 'no_key'
        value_del = 'no_key'
    elif ArrayOfKeys[index] != key:
        result_del = 'collision'
        for i in range(index + 1, len(ArrayOfKeys)):
            if ArrayOfKeys[i] == key:
                ArrayOfKeys[i] = None
                ArrayOfValues[i] = None
                HistoryArray[i] = 1
                value_del = 'removed'
                linear_probing = i
            elif HistoryArray[i] == -1:
                linear_probing = i
                break
        if linear_probing == len(ArrayOfKeys) - index - 1:
            result_del = 'no key with collision'
    return result_del, linear_probing, value_del


q, p, n = map(int, input().split())
ArrayOfKeys = [None] * q
ArrayOfValues = [None] * q
HistoryArray = [-1] * q
for i in range(n):
    command = list(input().split())
    if command[0] == 'PUT':
        hashed = hash_function(command[1], q, p)
        result, probing = put(hashed, command[1], command[2])
        if result == 'inserted':
            print('key=%s hash=%d operation=PUT result=inserted value=%s'%(command[1], hashed, command[2]))
        elif result == 'collision':
            print('key=%s hash=%d operation=PUT result=collision linear_probing=%d value=%s'%(command[1], hashed, probing, command[2]))
        elif result == 'overflow':
            print('key=%s hash=%d operation=PUT result=overflow'%(command[1], hashed))
    if command[0] == 'GET':
        hashed = hash_function(command[1], q, p)
        result, probing, value = get(hashed, command[1])
        if result == 'found':
            print('key=%s hash=%d operation=GET result=found value=%s' % (command[1], hashed, value))
        elif result == 'collision':
            print('key=%s hash=%d operation=GET result=collision linear_probing=%d value=%s' % (command[1], hashed, probing, value))
        elif result == 'no_key':
            print('key=%s hash=%d operation=GET result=%s' % (command[1], hashed, result))
    if command[0] == 'DEL':
        hashed = hash_function(command[1], q, p)
        result, probing, value = delete(hashed, command[1])
        if result == 'removed' or result == 'no_key':
            print('key=%s hash=%d operation=DEL result=%s' % (command[1], hashed, result))
        elif result == 'collision':
            print('key=%s hash=%d operation=DEL result=collision linear_probing=%d value=%s' % (command[1], hashed, probing, value))