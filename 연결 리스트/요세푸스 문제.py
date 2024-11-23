'''
import sys

N, K = map(int,sys.stdin.readline().split())

li = []
yose = []

for i in range(1, N+1):
    li.append(i)

cur = 0
while True:
    for i in range(K - 1):
        if cur >= len(li):
            cur = 0
        cur += 1
    if cur >= len(li):
        cur = 0
    yose.append(li[cur])
    li.remove(li[cur])
    if len(li) == 0:
        break

print("<", end="")
for i in range(N):
    if i == N-1:
        print(f"{yose[i]}", end="")
        break
    print(f"{yose[i]}", end=", ")
print(">")

'''

'''
7 3
=> <3, 6, 2, 7, 5, 1, 4>
'''

import sys
N, K = map(int,sys.stdin.readline().split())

li = [i for i in range(1, N+1)]

idx = 0
yose = []

for i in range(N):
    idx += K - 1
    idx %= len(li)
    yose.append(li.pop(idx))
    
print("<%s>" %(', '.join(map(str,yose))))