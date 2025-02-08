'''
문제
'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 
뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 
게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

입력
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 
맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며. 
게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. 
X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력
첫째 줄에 게임이 몇 초에 끝나는지 출력한다.
'''

import sys
from collections import deque
N = int(sys.stdin.readline())

board = [[0 for _ in range(N)] for _ in range(N)]

# 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
board[0][0] = 's'
snake_stack = deque()
snake_stack.append([0,0])
dir = 0 # 0(우) / 1(하) / 2(좌) / 3(상)


K = int(sys.stdin.readline())
for i in range(K):
    x,y = map(int,sys.stdin.readline().split())
    board[x-1][y-1] = 2 # 아이씨 0,0을 1행 1열로 두면 어떡해 헷갈리게 아오 -> 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

L = int(sys.stdin.readline())
direction = deque()
for i in range(L):
    direction.append(list(map(str,sys.stdin.readline().split())))

s = 0
fin_s, rotate = direction.popleft()
while True:
    x, y = snake_stack[-1][0], snake_stack[-1][1] # 뱀의 머리의 위치(스택의 최상단)
    s += 1
    if dir == 0: # 우
        if y+1 == N or board[x][y+1] == 's':
            # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
            break
        elif board[x][y+1] == 0:
            # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
            snake_stack.append([x,y+1])
            board[x][y+1] = 's'
            clean = snake_stack.popleft() # 꼬리가 위치한 칸 비우기
            board[clean[0]][clean[1]] = 0
        elif board[x][y+1] == 2:
            # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
            snake_stack.append([x,y+1])
            board[x][y+1] = 's'
    elif dir == 1: # 하
        if x+1 == N or board[x+1][y] == 's':
            # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
            break
        elif board[x+1][y] == 0:
            # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
            snake_stack.append([x+1,y])
            board[x+1][y] = 's'
            clean = snake_stack.popleft() # 꼬리가 위치한 칸 비우기
            board[clean[0]][clean[1]] = 0
        elif board[x+1][y] == 2:
            # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
            snake_stack.append([x+1,y])
            board[x+1][y] = 's'
    elif dir == 2: # 좌
        if y-1 < 0 or board[x][y-1] == 's':
            # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
            break
        elif board[x][y-1] == 0:
            # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
            snake_stack.append([x,y-1])
            board[x][y-1] = 's'
            clean = snake_stack.popleft() # 꼬리가 위치한 칸 비우기
            board[clean[0]][clean[1]] = 0
        elif board[x][y-1] == 2:
            # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
            snake_stack.append([x,y-1])
            board[x][y-1] = 's'
    else: # 상
        if x-1 < 0 or board[x-1][y] == 's':
            # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
            break
        elif board[x-1][y] == 0:
            # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
            snake_stack.append([x-1,y])
            board[x-1][y] = 's'
            clean = snake_stack.popleft() # 꼬리가 위치한 칸 비우기
            board[clean[0]][clean[1]] = 0
        elif board[x-1][y] == 2:
            # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
            snake_stack.append([x-1,y])
            board[x-1][y] = 's'
            
    if s == int(fin_s): # 게임 시작 시간으로부터 X초가 끝난 뒤에
        if rotate == 'L': # 왼쪽(C가 'L')으로 90도 방향을 회전
            dir = (dir + 3) % 4
        elif rotate == 'D': # 오른쪽(C가 'D')으로 90도 방향을 회전
            dir = (dir + 1) % 4
        if direction:
            fin_s, rotate = direction.popleft()
print(s)

'''
예제 입력 1 
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
예제 출력 1 
9
예제 입력 2 
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
예제 출력 2 
21
예제 입력 3 
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
예제 출력 3 
13

'''