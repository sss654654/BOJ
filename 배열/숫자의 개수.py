'''
import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

mul = A*B * C

mulstr = str(mul)

numarr = [0 for i in range(10)]

for i in mulstr:
    numarr[int(i)] += 1

for i in range(10):
    print(numarr[i])
'''


import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

abc_sum = A*B*C

num_dict = {}

for i in range(10):
    num_dict[i] = 0

while True:
    rem = abc_sum % 10
    abc_sum = int(abc_sum / 10)
    num_dict[rem] += 1
    if abc_sum == 0:
        break

for value in num_dict.values():
    print(value)