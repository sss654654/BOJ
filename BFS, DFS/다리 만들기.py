'''
입력
첫 줄에는 지도의 크기 N(100이하의 자연수)가 주어진다. 
그 다음 N줄에는 N개의 숫자가 빈칸을 사이에 두고 주어지며, 0은 바다, 1은 육지를 나타낸다. 
항상 두 개 이상의 섬이 있는 데이터만 입력으로 주어진다.

출력
첫째 줄에 가장 짧은 다리의 길이를 출력한다.
'''
import sys
N = int(sys.stdin.readline())
maps = []
for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))
visited = [[-1 for i in range(N)] for j in range(N)]

# 섬은 방문 처리(1), 바다는 거리 체크(1,2,3...)
from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque()
min_move = sys.maxsize
def BFS(x,y):
    global min_move
    q = deque()
    q.append([x,y])
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if visited[nx][ny] != -1:
                continue
            if maps[nx][ny] == 1 and maps[x][y] == 0: # 바다(육지)에서 육지로
                if min_move > visited[x][y]:
                    min_move = visited[x][y]
                continue
            elif maps[nx][ny] == 1 and maps[x][y] == 1: # 육지에서 육지로
                visited[nx][ny] = 0
                q.appendleft([nx,ny])
            elif maps[nx][ny] == 0 and maps[x][y] == 1: # 육지에서 바다로
                visited[nx][ny] = 1
                q.append([nx,ny])
            elif maps[nx][ny] == 0 and maps[x][y] == 0: # 바다에서 바다로
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx,ny])

def re_visited_water():
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0:
                visited[i][j] = -1

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and visited[i][j] == -1:
            BFS(i,j)
            re_visited_water() # A,B,C 섬이 있으면 A-B, A-C 만이 아닌 B-C도 비교해야 하므로 초기화

if min_move == sys.maxsize:
    print(0)
else:
    print(min_move)

'''
예제 입력 1 
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
예제 출력 1 
3

3
1 0 0
0 0 1
0 1 0
1

5
1 0 0 0 0
0 0 0 1 1
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
'''