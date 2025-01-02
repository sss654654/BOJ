'''
문제
당신은 상범 빌딩에 갇히고 말았다. 여기서 탈출하는 가장 빠른 길은 무엇일까? 
상범 빌딩은 각 변의 길이가 1인 정육면체(단위 정육면체)로 이루어져있다. 
각 정육면체는 금으로 이루어져 있어 지나갈 수 없거나, 비어있어서 지나갈 수 있게 되어있다. 
당신은 각 칸에서 인접한 6개의 칸(동,서,남,북,상,하)으로 1분의 시간을 들여 이동할 수 있다. 
즉, 대각선으로 이동하는 것은 불가능하다. 
그리고 상범 빌딩의 바깥면도 모두 금으로 막혀있어 출구를 통해서만 탈출할 수 있다.

당신은 상범 빌딩을 탈출할 수 있을까? 만약 그렇다면 얼마나 걸릴까?

입력
입력은 여러 개의 테스트 케이스로 이루어지며, 각 테스트 케이스는 세 개의 정수 L, R, C로 시작한다. 
L(1 ≤ L ≤ 30)은 상범 빌딩의 층 수이다. 
R(1 ≤ R ≤ 30)과 C(1 ≤ C ≤ 30)는 상범 빌딩의 한 층의 행과 열의 개수를 나타낸다.

그 다음 각 줄이 C개의 문자로 이루어진 R개의 행이 L번 주어진다. 
각 문자는 상범 빌딩의 한 칸을 나타낸다. 
금으로 막혀있어 지나갈 수 없는 칸은 '#'으로 표현되고, 비어있는 칸은 '.'으로 표현된다. 
당신의 시작 지점은 'S'로 표현되고, 탈출할 수 있는 출구는 'E'로 표현된다. 
각 층 사이에는 빈 줄이 있으며, 입력의 끝은 L, R, C가 모두 0으로 표현된다. 
시작 지점과 출구는 항상 하나만 있다.

출력
각 빌딩에 대해 한 줄씩 답을 출력한다. 만약 당신이 탈출할 수 있다면 다음과 같이 출력한다.

Escaped in x minute(s).
여기서 x는 상범 빌딩을 탈출하는 데에 필요한 최단 시간이다.

만일 탈출이 불가능하다면, 다음과 같이 출력한다.

Trapped!
'''
import sys

while True:
    L,R,C = map(int,sys.stdin.readline().split())
    if L == 0 and R == 0 and C == 0:
        break
    building = []
    visited = [[0 for i in range(C)] for j in range(L*R)]

    for i in range(L):
        for j in range(R):
            building.append(list(map(str,sys.stdin.readline().strip())))
        tmp = input()

    #for i in range(L*R):
    #    print(building[i])

    dx = [1,0,-1,0,R,-R]
    dy = [0,1,0,-1,0,0]

    from collections import deque

    result = -1

    def BFS(x,y):
        global result
        q = deque()
        q.append([x,y])
        visited[x][y] = 1
        while q: # L,R,C = 3,4,5 / dx = [1,0,-1,0,R,-R]
            x, y = q.popleft()
            for dir in range(6):
                nx = x + dx[dir]
                ny = y + dy[dir]
                floor = int(x/R)

                '''
                if dir <4:
                    ~~
                else:
                    ~~
                로 진행했으면 틀리지도 않고, 상하체크에서 절댓값을 사용안해도 되었을텐데..
                '''
                r = abs(dx[dir])
                if r == R: # 상,하
                    if nx<0 or nx>=L*R or ny<0 or ny>=C: # 0~L*R(전체)
                        continue
                else: # 동,서,남,북
                    if nx<R*floor or nx>=R*(floor+1) or ny<0 or ny>=C: # floor~floor*R(해당층만 서치)
                        continue
                if building[nx][ny] == '#' or visited[nx][ny] != 0:
                    continue
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx,ny])
                if building[nx][ny] == 'E':
                    result = visited[nx][ny]
                    break
            if result != -1:
                break

    for lr in range(L*R):
        for c in range(C):
            if building[lr][c] == 'S':
                BFS(lr,c)
    
    #for lr in range(L*R):
    #    print(visited[lr])
    
    if result == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {result-1} minute(s).")
'''

3 4 5
E....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####S

예제 입력 1 
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E

1 3 3
S##
#E#
###

0 0 0
예제 출력 1 
Escaped in 11 minute(s).
Trapped!
'''