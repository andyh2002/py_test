#! /usr/bin/env python
'''一年有多少天，这是个大问题，很值得思考。现在给你一个年份year(year为四位数字的字符串，如"2008","0012"),
你输出这一年的天数。如year="2013", 则输出365。
'''
year = "2100"
cnt = 0
if (int(year) % 4 == 0 and int(year) % 100 != 0)or int(year) % 400 == 0:
    cnt = 366
else:
    cnt = 365
print(cnt)
