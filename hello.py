def hanoi(n, a, b, c):
    if n == 1:
        print('Move', n, 'from', a, 'to', c)
    else:
        hanoi(n - 1, a, c, b)
        print('Move', n, 'from', a, 'to', c)
        hanoi(n - 1, b, a, c)

hanoi(8, 'Left', 'Mid', 'Right')
