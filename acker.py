#!/usr/bin/env python3

reclimit = int(input('What recursion limit should be implemented? '))

import sys
sys.setrecursionlimit(reclimit)

def acker(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return acker(m - 1, 1)
    else:
        return acker(m - 1, acker(m, n - 1))


a = int(input('To what m value should the ackermann function be iterated? '))
b = int(input('To what n value should the ackermann function be iterated? '))


for m in range(0, a + 1):
    for n in range(0, b + 1):
        x = acker(m, n)
        print('The value of ackermann (', m, ',', n, ') is', x, '!')
