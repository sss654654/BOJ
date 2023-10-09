import sys

N = int(sys.stdin.readline())

use = list(map(int,sys.stdin.readline().split()))

Y = 0
M = 0

for i in use:
    Yval = int(i / 30) + 1
    Y += Yval*10

    Mval = int(i / 60) + 1
    M += Mval*15

if Y == M:
    print("Y M {}".format(Y))
elif Y > M:
    print("M {}".format(M))
elif Y < M:
    print("Y {}".format(Y))