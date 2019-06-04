#! /usr/bin/env python
'''
给你一个整数组成的列表L，按照下列条件输出：
若L是升序排列的,则输出"UP";
若L是降序排列的,则输出"DOWN";
若L无序，则输出"WRONG"。
'''
L = [1, 3, 2]
c = 0
for i in range(len(L)-2):
    if L[i] < L[i+1]:
        c += 1
if c == len(L)-2:
    print('UP')
