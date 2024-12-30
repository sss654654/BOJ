'''
문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 
아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. 
(색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 
하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.
'''
import sys

N = int(sys.stdin.readline())
rgb = []
for i in range(N):
    rgb.append(list(map(str, sys.stdin.readline().strip())))
visited = [[0 for i in range(N)] for j in range(N)]
ab_visited = [[0 for i in range(N)] for j in range(N)]

from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

normal = 0
abnormal = 0

def BFS(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if rgb[x][y] != rgb[nx][ny] or visited[nx][ny] != 0:
                continue
            visited[nx][ny] = 1
            q.append([nx,ny])
def ab_BFS(x,y):
    q = deque()
    q.append([x,y])
    ab_visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if rgb[x][y] == 'R' or rgb[x][y] == 'G': # R or G
                if rgb[nx][ny] == 'B':
                    continue
            else: # B
                if rgb[x][y] != rgb[nx][ny]:
                    continue
            if ab_visited[nx][ny] != 0:
                continue
            ab_visited[nx][ny] = 1
            q.append([nx,ny])

for i in range(N):
    for j in range(N):
        if (rgb[i][j] == 'R' or rgb[i][j] == 'G' or rgb[i][j] == 'B') and visited[i][j] == 0:
            #print(rgb[i][j],i,j)
            BFS(i,j)
            normal += 1

for i in range(N):
    for j in range(N):
        if (rgb[i][j] == 'R' or rgb[i][j] == 'G' or rgb[i][j] == 'B') and ab_visited[i][j] == 0:
            #print(rgb[i][j],i,j)
            ab_BFS(i,j)
            abnormal += 1
print(normal, end=' ')
print(abnormal)

'''
5
RRRRR
RBBBR
RBGBR
RBBBR
RRRRR
3 3


예제 입력 1 
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
예제 출력 1 
4 3

2
GR
GR
2 1

3
RRG
GGR
GGR
4 1

2
RG
GR
4 1

5
RRRRR
RBBBR
RBGBR
RBBBR
RRRRR
3 3

3
GBG
GBG
RRR
4 2

3
RGB
RRR
RRR
3 2

20
BBBBBRRRRRRRRRRRBBBB
BBBBBRRRRRRRRRRRBBBB
RBBBBBRRRRRRRRRRBBBB
RRRBBBBRRRRRRRRRBBBB
RRRBBBBRRRRRRRRRRBRB
GRRBBBBRRRRRRRRRRBRR
GGRRRRBBBRRRRRRRRBBB
GGGRRRBBBRRRRRRRRBBB
RRGGGGBBBRRRRRRRRBBB
BBGGGGBBBBRRRRRRRBBB
BBGGGGGBBBRRRRRRRBBB
GBGGGGGBRRRRRRRRRBBB
GGGGGGGGRRRRRRRRRBBB
GGGGGGGGGRRRRRRRRBBB
GGGGGGGGGGRRRRRRRBBB
RRGGGGGGGGGGRRRRRRBB
RRGGGGGGGGGGGGGGGRBB
RRRGGGGGGGGGGGGGGRBB
GGGGGGGBGGGGGGGGGGBB
RRRRGGGGGGGGGGGGGGGG
11 6

5
RRRBB
GRBBB
BBBRR
BBRRR
RRRRR
4 3

5
GGGGG
GGGGG
GGGGG
GGGRB
GGGGG
3 2

3
RRR
RGR
RRR
2 1

5
BBBBG
GRBBB
BBBBB
BBBBB
RRRRR
5 4

2
RG
GR
4 1

3
RRR
BBB
GGG
3 3

5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
4 3

5
RRRRR
RRRRR
RRRRR
RRRRR
RRRRR
1 1

5
RRRRR
RRRRR
RRGRR
RRRRR
RRRRR
2 1

5
RRRRR
RRRRR
RRBRR
RRRRR
RRRRR
2 2

5
RRRRR
RBBBR
RBGBR
RBBBR
RRRRR
3 3

5
RRRRR
RGGGR
RGBGR
RGGGR
RRRRR
3 2

5
BBBBB
BBGBG
BGGGG
BBRRR
RRRRR
3 2

2
RG
BR
4 2

1
R
1 1

5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
4 3

5
RRGRR
RGGGR
GGRGG
GRRRG
GRRRG
4 1
'''