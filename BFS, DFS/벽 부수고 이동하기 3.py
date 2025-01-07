'''
문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다. 
이동하지 않고 같은 칸에 머물러있는 경우도 가능하다. 이 경우도 방문한 칸의 개수가 하나 늘어나는 것으로 생각해야 한다.

이번 문제에서는 낮과 밤이 번갈아가면서 등장한다. 가장 처음에 이동할 때는 낮이고, 한 번 이동할 때마다 낮과 밤이 바뀌게 된다.
이동하지 않고 같은 칸에 머무르는 경우에도 낮과 밤이 바뀌게 된다. -> ??

만약에 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다. 
단, 벽은 낮에만 부술 수 있다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000), K(1 ≤ K ≤ 10)이 주어진다. 
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
'''

import sys
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M,K = map(int, sys.stdin.readline().split())
maps = []
for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().strip())))
visited = [[[0] * (M) for _ in range(N)] for _ in range(K+1)] # [k][N][M]

def BFS():
    q = deque()
    q.append([0,0,0,1]) # [x,y,k,d] # d=1 낮, d=2 밤, d=3 낮, d=4 밤....
    visited[0][0][0] = 1
    while q:
        x,y,k,day = q.popleft()
        night = day % 2 # night가 0이면(짝수) 밤
        if x == N-1 and y == M-1:
            return day
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if maps[nx][ny] == 0 and visited[k][nx][ny] == 0:
                visited[k][nx][ny] = day
                q.append([nx,ny,k,day+1])
            elif k < K and maps[nx][ny] == 1 and visited[k+1][nx][ny] == 0:
                if night:
                    visited[k+1][nx][ny] = day
                    q.append([nx,ny,k+1,day+1])
                else:
                    q.append([x,y,k,day+1])
    return -1
print(BFS())


'''
예제 입력 1 
1 4 1
0010 -> 낮(밤낮)밤낮
예제 출력 1 
5
예제 입력 2 
1 4 1
0100
예제 출력 2 
4
예제 입력 3 
6 4 1
0100
1110
1000
0000
0111
0000
예제 출력 3 
15
예제 입력 4 
6 4 2
0100
1110
1000
0000
0111
0000
예제 출력 4 
9
'''