def hanoi(n, a, b, c):
    """
    汉诺塔
    :param n: 汉诺塔的层数
    :param a:左边
    :param b:中间
    :param c:右边
    :return:打印汉诺塔的移动过程
    """
    if n == 1:
        print('Move', n, 'from', a, 'to', c)
    else:
        hanoi(n - 1, a, c, b)
        print('Move', n, 'from', a, 'to', c)
        hanoi(n - 1, b, a, c)


# 调用测试
hanoi(10, 'Left', 'Mid', 'Right')
