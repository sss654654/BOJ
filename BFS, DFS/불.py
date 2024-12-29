'''
문제
지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!

미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 
그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.

지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다.

불은 각 지점에서 네 방향으로 확산된다.

지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.

지훈이와 불은 벽이 있는 공간은 통과하지 못한다.

입력
입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. 
R은 미로 행의 개수, C는 열의 개수이다.

다음 입력으로 R줄동안 각각의 미로 행이 주어진다.

각각의 문자들은 다음을 뜻한다.

#: 벽
.: 지나갈 수 있는 공간
J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
F: 불이 난 공간
J는 입력에서 하나만 주어진다.

출력
지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.
지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.
'''
# dfs?

import sys

R, C = map(int, sys.stdin.readline().split())

laby = []

for i in range(R):
    tmp = list(map(str, sys.stdin.readline().strip()))
    laby.append(tmp)

visited_j = [[0 for i in range(C)] for j in range(R)]
visited_fire = [[0 for i in range(C)] for j in range(R)]

from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

q = deque()
def BFS():
    global q
    # 지훈이가 행동하고 불이 퍼저야 돼
    while q:
        # print(q)
        x, y, check = q.popleft()
        if check == 'j': # 지훈이
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    return visited_j[x][y]
                if laby[nx][ny] == '#' or visited_fire[nx][ny] != 0: 
                    # 지훈이는 벽이 아니고 불이 아닌 곳으로 이동 가능 이외 다른 조건 불필요
                    continue
                if visited_fire[x][y] == visited_j[x][y]:
                    # 지훈이가 움직였던 곳(x,y)에 불이 붙었을 경우
                    continue
                visited_j[nx][ny] = visited_j[x][y] + 1
                q.append([nx,ny,'j'])
                '''
                print('j')
                for i in range(R):
                    print(visited_j[i])
                print('fire')
                for i in range(R):
                    print(visited_fire[i])
                '''
        else: # 불
            for dir in range(4): # 불은 네방향으로 퍼지니까
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                if laby[nx][ny] == '#' or visited_fire[nx][ny] != 0: 
                    # 불도 벽이 아니고 불이 아닌 곳으로 네방향 이동 가능
                    continue
                visited_fire[nx][ny] = visited_fire[x][y] + 1
                q.append([nx,ny,'fire'])
    return 0


result = 0

for x in range(R):
    for y in range(C):
        if laby[x][y] == 'J':
            q.append([x,y,'j'])
            visited_j[x][y] = 1
        if laby[x][y] == 'F':
            q.appendleft([x,y,'fire']) # 불이 먼저 번져야 지훈이의 이동 경로 체크가 쉬울듯
            visited_fire[x][y] = 1
result = BFS()   

if result == 0:
    print("IMPOSSIBLE")
else:
    print(result)

'''
예제 입력 1 
4 4
####
#JF#
#..#
#..#

3

4 4
####
#J.#
#.F#
#..#

impossible

17 5
#....
F....
#.#..
.....
.....
.....
.....
.....
.....
.....
.....
#...#
F...#
.....
.....
#J...
F.#..

4

5 6
######
#...J#
#.F..#
#....#
#....#

4

10 100
....................................................................................................
.......###############.......FFFF..........########.................................................
.........FFFFFFFFFFFFF#############...........................FFF..........##########....########...
.....................................................................######..................####...
.......FF...................................J.......................................................
.............................................................................................####...
......................###############################################...............................
....................................................................................................
.........FFFFFFFFFFFFF............####..........................................FFFFFF....FFFFF.....
.............................................###.######.............................................

7

'''