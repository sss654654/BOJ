import sys

N = int(sys.stdin.readline())

for i in range(N):
    for j in range(N-1-i):
        print(" ",end ="")
        
    for k in range((i+1)*2 - 1):
        print("*",end ="")
    print()