'''
문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 
그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 
두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. 
(단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 
단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
'''

import sys
n, m = map(int,sys.stdin.readline().split())
art = []
for ndx in range(n): # 세로
    art.append(list(map(int,sys.stdin.readline().split())))
visited = [[0 for j in range(m)] for i in range(n)]

# print(art)
# print(visited)

''' ************dfs => 재귀***********
art_count = 0
big_art = 0
art_depth = 0

def dfs(x, y):
    global art_depth
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if art[x][y] == 1 and visited[x][y] == 0:
        art_depth += 1
        visited[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            if big_art < art_depth:
                big_art = art_depth
            art_depth = 0
            art_count += 1
            # print(f"[{i},{j}]")

print(art_count)
print(big_art)
'''

# **********bfs => 큐************
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

art_depth = 0

def BFS(x, y):
    global art_depth
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    depth_count = 1
    while q: # n:6, m:5
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 1 or art[nx][ny] == 0:
                # 이미 방문한 곳, 그림이 아닌 곳은 무시 -> continue
                continue
            visited[nx][ny] = 1
            q.append([nx, ny])
            depth_count += 1
    if art_depth < depth_count:
        art_depth = depth_count
art_count = 0

for i in range(n):
    for j in range(m):
        if art[i][j] == 1 and visited[i][j] == 0:
            BFS(i,j)
            art_count += 1

print(art_count)
print(art_depth)

'''
예제 입력 1 
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

예제 출력 1 
4
9
'''