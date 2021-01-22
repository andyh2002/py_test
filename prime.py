import math

count = 0
num = 2

x = int(input("请输入小于50的数："))
# while count < x:
#     for i in range(2, x):
#         if x % i == 0:
#             print("{} is not a prime!".format(count))
#             break
#     else:
#         print('{} is a prime'.format(count))
#     count += 1


for n in range(2, x):
    for i in range(2, n):
        if n % i == 0:
            print("{} equals {}*{}".format(n, i, n // i))
            break
    else:
        print('{} is a prime'.format(n))
