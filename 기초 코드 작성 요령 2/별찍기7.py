import sys

N = int(sys.stdin.readline())

for i in range(1,2*N):
    for j in range(abs(N-i)):
        print(" ",end ="")
    if i <= N:
        for k in range(2*i -1):
            print("*",end ="")
    else:
        rem = (i) % N
        for k in range(2*(N - rem) - 1) :
            print("*",end ="")
        
    print()