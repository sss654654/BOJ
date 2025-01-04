
'''
벽 부수고 이동하기

문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
'''
import sys
N, M = map(int, sys.stdin.readline().split())
maps = []

for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().strip())))
visited = [[[0 for i in range(2)] for j in range(M)] for k in range(N)]

# [벽을 부수지 않은 세계, 벽을 부순 세계](6,4)
'''
for i in range(N):
    print(visited[i])
[[0, 0], [0, 0], [0, 0], [0, 0]]
[[0, 0], [0, 0], [0, 0], [0, 0]]
[[0, 0], [0, 0], [0, 0], [0, 0]]
[[0, 0], [0, 0], [0, 0], [0, 0]]
[[0, 0], [0, 0], [0, 0], [0, 0]]
[[0, 0], [0, 0], [0, 0], [0, 0]]
'''

from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1 # 벽을 부수지 않은 셰게에서부터 시작
    while q:
        x,y,world = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][world]
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if visited[nx][ny][world] != 0 :
                continue
            if world == 0 and maps[nx][ny] == 1: # 벽을 부수지 않은 세계에서 벽을 만날 경우 세계 변환
                # 벽을 부수지 않은 세계에서 벽을 부순 세계로 넘어감([world] -> [1])
                visited[nx][ny][1] = visited[x][y][world] + 1
                q.append([nx,ny,1])
            elif maps[nx][ny] == 0: # 어떤 세계든 벽이 안막혀있으면 진행
                visited[nx][ny][world] = visited[x][y][world] + 1
                q.append([nx,ny,world])
    return -1

print(BFS())

'''
예제 입력 1 
6 4
0100
1110
1000
0000
0111
0000
예제 출력 1 
15
예제 입력 2 
4 4
0111
1111
1111
1110
예제 출력 2 
-1
'''