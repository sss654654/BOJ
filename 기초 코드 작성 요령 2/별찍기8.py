import sys
N = int(sys.stdin.readline())


for i in range(1,2*N):
    if i < N:
        for j in range(i):
            print("*",end ="")
        for k in range(2*(N-i)):
            print(" ",end ="")
        for l in range(i):
            print("*",end ="")
    elif i == N:
        for j in range(2*N):
            print("*",end ="")
    else:
        temp = abs(N - i)
        for j in range(N -temp):
            print("*",end ="")
        for k in range(2*temp):
            print(" ",end ="")
        for l in range(N -temp):
            print("*",end ="")
    print()
