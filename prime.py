import math
count = 0
num = 2

x = int(input("请输入小于50的数："))
while count < 50:
    for i in range(2, x):
        if x % i == 0:
            print("x is not a prime!")
            break
        else:
            print('x is a prime')
