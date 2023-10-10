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
