import sys

N = int(sys.stdin.readline())

for i in range(N):
    for k in range(N-i):
        print("*",end ="")
    print()