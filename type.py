def f(x, y, o):
    return {
        '+': {
            (int, float): 'plus 1',
            (float, int): 'plus 2',
            }[x, y],
        '-': {
            (int, float): 'min 1',
            (float, int): 'min 2',
            }[x, y]
    }[o]

# myDict = {'England': 435, 'France': 12, 'Egypt': 31}

# tup = [(key, value) for key, value in myDict.items()]

print(f(float, int, '+'))