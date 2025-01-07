'''
문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000), K(1 ≤ K ≤ 10)이 주어진다. 
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
'''

import sys
N, M, K = map(int, sys.stdin.readline().split())
maps = []
for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().strip())))
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

# visited[K][N][M]
'''
N, M, K = 1000, 1000, 10

visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)] # visited[1000][1000][11]
print(asizeof.asizeof(visited)) # 153025040 (≈ 153.0MB)

visited = [[[0] * (M) for _ in range(N)] for _ in range(K+1)] # visited[11][1000][1000]
print(asizeof.asizeof(visited)) # 88715384 (≈ 88.7MB)
'''
from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1
    while q:
        x,y,k = q.popleft()
        if x==N-1 and y==M-1:
            return visited[x][y][k]
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if k != K and maps[nx][ny] == 1 and visited[nx][ny][k+1]== 0:
                visited[nx][ny][k+1] = visited[x][y][k] + 1
                q.append([nx,ny,k+1])
            elif maps[nx][ny] == 0 and visited[nx][ny][k] == 0:
                if k != 0:
                    if visited[nx][ny][k-1] != 0:
                        continue
                visited[nx][ny][k] = visited[x][y][k] + 1
                q.append([nx,ny,k])

    return -1
print(BFS())
for i in range(N):
    print(visited[i])
'''
for i in range(K+1):
    for j in range(N):
        print(visited[i][j])
    print()
'''
'''
예제 입력 1 
6 4 1
0100
1110
1000
0000
0111
0000
예제 출력 1 
15
예제 입력 2 
6 4 2
0100
1110
1000
0000
0111
0000
예제 출력 2 
9
예제 입력 3 
4 4 5
0111
1111
1111
1110
예제 출력 3 
-1
'''

from collections import deque
import sys

n, m, k = map(int, input().split())
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
d = deque([(0, 0, 0, 1)]) # k, n, m, 현재까지의 거리
visited[0][0][0] = 1

while d:
  ck, cn, cm, dist = d.popleft()  # dist : 밤/낮 정보이자 거리정보
  # 도착
  if cn == n - 1 and cm == m - 1:
    print(dist)
    break

  # 탐색
  day = dist % 2  # dist가 짝수면 밤
  for dn, dm in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
    nn, nm = cn + dn, cm + dm
    if (0 <= nn < n and 0 <= nm < m):
      # 일반 탐색
      if visited[ck][nn][nm] == 0 and graph[nn][nm] == 0:
        visited[ck][nn][nm] = dist
        d.append((ck, nn, nm, dist + 1))

      # 첫 방문인 벽 부수기
      elif (ck < k and graph[nn][nm] == 1 and visited[ck + 1][nn][nm] == 0):
        # 낮이라면
        if day:
          visited[ck + 1][nn][nm] = dist
          d.append((ck + 1, nn, nm, dist + 1))
        # 밤이라면
        else:
          d.append((ck, cn, cm, dist + 1)) # 하루 대기

else:
  print(-1)