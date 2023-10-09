import sys
N = int(sys.stdin.readline())


for i in range(1,2*N):
    if i < N:
        for k in range(i-1):
            print(" ",end ="")
        for j in range(2*N - (2*i -1)):
            print("*",end ="")
    elif i == N:
            for j in range(i-1):
                print(" ",end ="")
            print("*",end ="")
    else:
        temp = abs(N - 1-i)
        for k in range(N - temp):
            print(" ",end ="")
        for l in range(2*temp - 1):
            print("*",end ="")
    print()
