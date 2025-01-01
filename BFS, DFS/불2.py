'''
문제
상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다. 건물의 일부에는 불이 났고, 상근이는 출구를 향해 뛰고 있다.

매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 벽에는 불이 붙지 않는다. 
상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다. 
상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 
상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.

빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.

각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)

다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.

'.': 빈 공간
'#': 벽
'@': 상근이의 시작 위치
'*': 불
각 지도에 @의 개수는 하나이다.

출력
각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다. 
빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.
'''
import sys
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

T = int(sys.stdin.readline())
for i in range(T):
    w, h = map(int, sys.stdin.readline().split()) # 너비(w), 높이(h)
    building = []
    visited_s = [[0 for i in range(w)] for i in range(h)]
    visited_fire = [[0 for i in range(w)] for i in range(h)]
    for j in range(h):
        building.append(list(map(str,sys.stdin.readline().strip())))
   
    q = deque()
    move = 0
    def BFS():
        global q, move
        while q:
            x, y, check = q.popleft()
            if check == 's':
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if nx<0 or nx>=h or ny<0 or ny>=w:
                        return visited_s[x][y]
                    if building[nx][ny] != '.' or visited_s[nx][ny] != 0 or visited_fire[nx][ny] != 0:
                        # 빈공간이 아니거나, 상근이가 이미 방문한 곳이거나, 불이 이미 퍼진곳이면 넘어가
                        continue
                    visited_s[nx][ny] = visited_s[x][y] + 1
                    q.append([nx,ny,'s'])
            elif check == 'fire':
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if nx<0 or nx>=h or ny<0 or ny>=w:
                        continue
                    if building[nx][ny] != '.' or visited_fire[nx][ny] != 0:
                        # 빈공간이 아니거나, 불이 이미 퍼진곳이면 넘어가
                        continue
                    visited_fire[nx][ny] = visited_fire[x][y] + 1
                    q.append([nx,ny,'fire'])
                    '''
            for i in range(h):
                print(visited_s[i])
            print()
            for i in range(h):
                print(visited_fire[i])
                '''
        return 0

    result = 0
    for x in range(h):
        for y in range(w):
            if building[x][y] == '@':
                q.append([x,y,'s'])
                visited_s[x][y] = 1
            if building[x][y] == '*':
                q.appendleft([x,y,'fire'])
                visited_fire[x][y] = 1
    result = BFS()
    '''
    for i in range(h):
        print(visited_s[i])
    print()
    for i in range(h):
        print(visited_fire[i])
    '''
    
    if result == 0:
        print("IMPOSSIBLE")
    else:
        print(result)

'''
예제 입력 1 
5
4 3
####
#*@.
####
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
7 4
###.###
#....*#
#@....#
.######
5 5
.....
.***.
.*@*.
.***.
.....
3 3
###
#@#
###
예제 출력 1 
2
5
IMPOSSIBLE
IMPOSSIBLE
IMPOSSIBLE
'''