'''
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?



입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
체스판의 크기는 l × l이다. 
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
'''
import sys

t = int(sys.stdin.readline())

dx = [2,1,-1,-2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]

from collections import deque

for i in range(t):
    N = int(sys.stdin.readline())
    knight_x, knight_y = map(int,sys.stdin.readline().split())
    move_x, move_y = map(int,sys.stdin.readline().split())
    chess = [[0 for i in range(N)] for j in range(N)]
    visited = [[0 for i in range(N)] for j in range(N)]
    chess[knight_x][knight_y] = 1
    def BFS(x,y):
        q = deque()
        q.append([x,y])
        visited[x][y] = 1
        while q:
            x, y = q.popleft()
            if move_x == x and move_y == y:
                print(visited[x][y]-1)
                break
            for dir in range(8):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue
                if visited[nx][ny] != 0:
                    continue
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx,ny])

    BFS(knight_x, knight_y)


'''
예제 입력 1 
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
예제 출력 1 
5
28
0
'''