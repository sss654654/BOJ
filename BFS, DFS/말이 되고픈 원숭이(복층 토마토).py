'''
문제
동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다. 그 녀석은 말(Horse)이 되기를 간절히 원했다. 그래서 그는 말의 움직임을 유심히 살펴보고 그대로 따라 하기로 하였다. 말은 말이다. 말은 격자판에서 체스의 나이트와 같은 이동방식을 가진다. 다음 그림에 말의 이동방법이 나타나있다. x표시한 곳으로 말이 갈 수 있다는 뜻이다. 참고로 말은 장애물을 뛰어넘을 수 있다.

 	x	 	x	 
x	 	 	 	x
 	 	말	 	 
x	 	 	 	x
 	x	 	x	 
근데 원숭이는 한 가지 착각하고 있는 것이 있다. 말은 저렇게 움직일 수 있지만 원숭이는 능력이 부족해서 총 K번만 위와 같이 움직일 수 있고, 그 외에는 그냥 인접한 칸으로만 움직일 수 있다. 대각선 방향은 인접한 칸에 포함되지 않는다.

이제 원숭이는 머나먼 여행길을 떠난다. 격자판의 맨 왼쪽 위에서 시작해서 맨 오른쪽 아래까지 가야한다. 인접한 네 방향으로 한 번 움직이는 것, 말의 움직임으로 한 번 움직이는 것, 모두 한 번의 동작으로 친다. 격자판이 주어졌을 때, 원숭이가 최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 방법을 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 정수 K가 주어진다. 둘째 줄에 격자판의 가로길이 W, 세로길이 H가 주어진다. 
그 다음 H줄에 걸쳐 W개의 숫자가 주어지는데, 0은 아무것도 없는 평지, 1은 장애물을 뜻한다. 
장애물이 있는 곳으로는 이동할 수 없다. 시작점과 도착점은 항상 평지이다. W와 H는 1이상 200이하의 자연수이고, 
K는 0이상 30이하의 정수이다.

출력
첫째 줄에 원숭이의 동작수의 최솟값을 출력한다. 시작점에서 도착점까지 갈 수 없는 경우엔 -1을 출력한다.
'''

import sys
from collections import deque

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
monkey = []
for i in range(H):
    monkey.append(list(map(int, sys.stdin.readline().split())))
visited = [[[0 for i in range(K+1)] for j in range(W)] for k in range(H)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

h_dx = [2,1,-1,-2,-2,-1,1,2]
h_dy = [1,2,2,1,-1,-2,-2,-1]

def BFS():
    q = deque()
    # 원숭이는 K+1의 각 층에서 움직이며 처음은 맨 아랫층에서 시작
    q.append([0,0,0])
    visited[0][0][0] = 1
    while q:
        x,y,k = q.popleft()
        if x == H-1 and y == W-1:
            return visited[x][y][k] - 1
        if K != k:
            for dir in range(8):
                nx = x + h_dx[dir]
                ny = y + h_dy[dir]
                if nx<0 or nx>=H or ny<0 or ny>=W:
                    continue
                if monkey[nx][ny] != 0 or visited[nx][ny][k+1] != 0:
                    continue
                visited[nx][ny][k+1] = visited[x][y][k] + 1 # 말처럼 움직일 시 다음 층으로 이동
                q.append([nx,ny,k+1])
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or nx>=H or ny<0 or ny>=W:
                continue
            if monkey[nx][ny] != 0 or visited[nx][ny][k] != 0:
                continue
            visited[nx][ny][k] = visited[x][y][k] + 1
            q.append([nx,ny,k])   
    return -1         

print(BFS())

'''
import sys
from collections import deque

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
monkey = []
for i in range(H):
    monkey.append(list(map(int, sys.stdin.readline().split())))
visited = [[[0 for m in range(K+1)] for i in range(W)] for j in range(H)]
# K가 2면 [점프 2번남은 원숭이, 점프 1번남은 원숭이, 점프 다한 원숭이]가 각각 맵을 탐색

dx = [1,0,-1,0]
dy = [0,-1,0,1]

h_dx = [2,1,-1,-2,-2,-1,1,2]
h_dy = [1,2,2,1,-1,-2,-2,-1]

def BFS():
	global K
	q = deque()
	q.append([0,0,0])
	visited[0][0][0] = 1
	# 원숭이가 언제 말처럼 움직여야 하는지를 어떻게 구현하지?
	while q:
		x, y, k = q.popleft()
		if x == H-1 and y == W-1:
			return visited[x][y][k]-1
		if k != K: # 점프는 점프대로 횟수가 남았다면 점프를 해서 층(k)이 오른채로 큐에 삽입
			for dir in range(8):
				nx = x + h_dx[dir]
				ny = y + h_dy[dir]
				if nx<0 or nx>=H or ny<0 or ny>=W:
					continue
				if monkey[nx][ny] != 0 or visited[nx][ny][k+1] != 0:
					continue
				visited[nx][ny][k+1] = visited[x][y][k] + 1
				q.append([nx,ny,k+1])
		# 근데 이제 가장 중요한 것은 점프를 한 원숭이는 이제 윗층으로 복사되었다는 것
		# 1층의 원숭이는 점프횟수를 기억한채로 계속 움직임
		# 점프한 원숭이는 점프한 층에서 계속 움직임
		# 원숭이는 위의 조건문에서 점프를 해서 복사되어 다른 층에 도달
		# 점프하지 않은 기본 원숭이는 그대로 해당 층에서 BFS 탐색 후 큐에 삽입
		# 이 원숭이는 아직 점프 기회가 남아있으므로 다음 큐에서 꺼내질 때 점프할 것
		# 즉, 원숭이가 어떤 자리에서든 말처럼 점프할 수 있게되며 도착점에 도달할 수 있게 됨
		for dir in range(4):
			nx = x + dx[dir]
			ny = y + dy[dir]
			if nx<0 or nx>=H or ny<0 or ny>=W:
				continue
			if monkey[nx][ny] != 0 or visited[nx][ny][k] != 0:
				continue
			visited[nx][ny][k] = visited[x][y][k] + 1
			q.append([nx,ny,k])
	return -1

print(BFS())

for i in range(H):
	print(visited[i])
'''

'''
2
9 2
0 0 1 0 0 1 0 1 0
0 0 1 1 0 0 0 1 0

2
10 2
0 0 1 0 0 1 0 0 1 0
0 0 1 1 0 0 0 0 1 0

10

예제 입력 1 
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
예제 출력 1 
4
예제 입력 2 
2
5 2
0 0 1 1 0
0 0 1 1 0
예제 출력 2 
-1


'''