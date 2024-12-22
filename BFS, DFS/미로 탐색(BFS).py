'''
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 
최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
'''

import sys

N, M = map(int, sys.stdin.readline().split())
rabi = []
for i in range(N):
    rabi.append(list(map(int,sys.stdin.readline().strip())))
visited = [[0 for j in range(M)] for i in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

from collections import deque

def BFS(x,y):
    q = deque()
    q.append([x,y,1])
    visited[x][y] = 1
    while q:
        x, y, dist = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] != 0 or rabi[nx][ny] == 0:
                continue
            visited[nx][ny] = dist + 1
            q.append([nx,ny,visited[nx][ny]])

BFS(0,0)
#for i in range(N):
#    print(visited[i])
print(visited[N-1][M-1])


'''
def dfs(x,y,dist):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if rabi[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = dist # 거리를 visited에 구현하면 될듯?
        dfs(x-1,y,dist+1) # 좌
        dfs(x, y-1,dist+1) # 하
        dfs(x+1,y,dist+1) # 우
        dfs(x,y+1,dist+1) # 상
        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i,j,1) == True:
            print(i, j)

for i in range(N):
    print(visited[i])
print(visited[N-1][M-1])
# 아 bfs네
'''

'''
예제 입력 1 
4 6
101111
101010
101011
111011
예제 출력 1 
15
예제 입력 2 
4 6
110110
110110
111111
111101
예제 출력 2 
9
예제 입력 3 
2 25
1011101110111011101110111
1110111011101110111011101
예제 출력 3 
38
예제 입력 4 
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
예제 출력 4 
13
'''