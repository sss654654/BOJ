import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
visited = [0 for i in range(100001)]
dx = [2,1,-1]

def BFS():
    q = deque()
    q.append([N])
    visited[N] = 1
    while q:
        x_list = q.popleft()
        x = x_list[-1]
        if x == K:
            print(visited[x] - 1)
            print(' '.join(map(str,x_list)))
            return 0
        for dir in range(3):
            nx = 0
            if dir == 0:
                nx = x*dx[dir]
            elif dir == 1:
                nx = x+dx[dir]
            else:
                nx = x+dx[dir]
            if nx<0 or nx>=100000:
                continue
            if visited[nx] != 0:
                continue
            # [5,10] [5,6] [5,4]
            visited[nx] = visited[x] + 1
            tmp = x_list[:] # 같은 리스트를 참조하지 않도록 하는 방법 -> [:]
            tmp.append(nx)
            q.append(tmp)
'''
4
5 10 9 18 17
'''
BFS()