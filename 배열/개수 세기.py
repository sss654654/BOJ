import sys

N = int(sys.stdin.readline())

intarr = list(map(int,sys.stdin.readline().split()))

v = int(sys.stdin.readline())

ans = 0

intarr.sort()

for i in intarr:
    if ans == 0:
        if i == v:
            ans+= 1
    else:
        if i == v:
            ans+= 1
        else:
            break

print(ans)