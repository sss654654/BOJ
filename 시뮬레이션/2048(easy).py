'''
입력
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 
0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다.
블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.

출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
'''
import sys

N = int(sys.stdin.readline())
playing_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 5번의 기회 각각 상하좌우로 이동 -> 4^5 = 1024
# 4진법?

move_stack = []

from collections import deque
def update(k, board):
    return_board = [[0 for _ in range(N)] for _ in range(N)]
    if k == 1: # 게임판을 우측으로 기울이기
        for x in range(N):
            stack = deque()
            for y in range(N-1,-1,-1): # 보드의 우측에서부터 좌측방향으로 숫자 탐색
                if stack: # 스택에 값이 들어있다면
                    if stack[-1][0] == board[x][y] and stack[-1][1] == 0: 
                        # 스택의 최상단과 넣으려는 값이 같으면 and 합쳐진 적이 없으면(0이면)
                        tmp = stack.pop()
                        stack.append([tmp[0]+board[x][y],1]) # 합친 수는 1로 스택에 넣어 조건에서 걸러지도록 함
                        continue
                if board[x][y] != 0: # 숫자가 0이 아니라면 스택에 값과 0을 함께 넣음
                    stack.append([board[x][y],0]) # 합쳐지지 않은 수는 0

            tmp_y = N - 1
            while stack: # 스택이 빌 때까지 반복
                tmp = stack.popleft() # 제일 먼저 스택에 쌓인 순서대로 보드를 다시 구성
                return_board[x][tmp_y] = tmp[0] # 우측으로 게임판을 기울어야 하므로 우측에서부터 값 대입
                tmp_y -= 1
            for i in range(tmp_y, -1,-1): # 스택에 있는 계산되고 넣어진 값들이 보드에 모두 소모되고 나머지는 0으로 표기 
                return_board[x][i] = 0
        return return_board # 우측으로 기울어진 보드를 반환, 이하 생략
    elif k == 2: # 좌
        for x in range(N):
            stack = deque()
            for y in range(N):
                if stack:
                    if stack[-1][0] == board[x][y] and stack[-1][1] == 0: # 스택의 최상단과 넣으려는 값이 같으면
                        tmp = stack.pop()
                        stack.append([tmp[0]+board[x][y],1])
                        continue
                if board[x][y] != 0:
                    stack.append([board[x][y],0])
            tmp_y = 0
            while stack:
                tmp = stack.popleft()
                return_board[x][tmp_y] = tmp[0]
                tmp_y += 1
            for i in range(tmp_y, N):
                return_board[x][i] = 0
        return return_board
    elif k == 3: # 하
        for y in range(N):
            stack = deque()
            for x in range(N-1,-1,-1):
                if stack:
                    if stack[-1][0] == board[x][y] and stack[-1][1] == 0: # 스택의 최상단과 넣으려는 값이 같으면
                        tmp = stack.pop()
                        stack.append([tmp[0]+board[x][y],1])
                        continue
                if board[x][y] != 0:
                    stack.append([board[x][y],0])
            tmp_x = N - 1
            while stack:
                tmp = stack.popleft()
                return_board[tmp_x][y] = tmp[0]
                tmp_x -= 1
            for i in range(tmp_x,-1,-1):
                return_board[i][y] = 0
        return return_board
    elif k == 4: # 상
        for y in range(N):
            stack = deque()
            for x in range(N):
                if stack:
                    if stack[-1][0] == board[x][y] and stack[-1][1] == 0: # 스택의 최상단과 넣으려는 값이 같으면
                        tmp = stack.pop()
                        stack.append([tmp[0]+board[x][y],1])
                        continue
                if board[x][y] != 0:
                    stack.append([board[x][y],0])
            tmp_x = 0
            while stack:
                tmp = stack.popleft()
                return_board[tmp_x][y] = tmp[0]
                tmp_x += 1
            for i in range(tmp_x, N):
                return_board[i][y] = 0
        return return_board

# 백트래킹으로 파고들어야겠는데
# update(1)이 update(1) update(2) update(3) update(4)를 불러야 하고 이는 다섯번 반복
# k=0, i=1 -> k=1 i=1 -> k=2 i=1 -> k=3 i=1 (-> k=4 i=1 -> k=4 i=2 -> k=4 i=3 -> k=4 i=3 k=4 i=4)
# 업데이트 하기 전의 배열의 상태를 저장해야 돼

max_val = 0
tmp = playing_board.copy()
def play(k):
    global max_val, tmp
    if k == 5:
        for i in range(N):
            for j in range(N):
                if max_val < tmp[i][j]:
                    max_val = tmp[i][j]
        return
    for i in range(1,5):
        prev_tmp = tmp # 업데이트 되기 전 보드판을 prev_tmp에 저장
        tmp = update(i,tmp) # 어떤 방향에 대해 업데이트된(기울어진) 보드판을 tmp에 저장
        play(k+1) # 이 행위가 5번이 반복될 때까지 함수 호출(백트래킹)
        # k가 5가 되면 보드판에서 최댓값을 구한 후 리턴
        tmp = prev_tmp # 리턴된 즉시 업데이트 전 보드판(prev_tmp)를 현재 보드판(tmp)에 롤백하여 다시 다른 방향에 대해서 업데이트 수행
    return # k에서 반복문을 다 돌았으면 k-1로 돌아가

play(0)
print(max_val)

# k = 0,1,2,3,4
'''
play(0)
update(1,playing_board)
for i in range(N):
    print(playing_board[i])
print()
update(1,playing_board)
for i in range(N):
    print(playing_board[i])
'''

'''
4
2 4 16 8
8 4 0 0
16 8 2 0
2 8 2 0

우
[2, 4, 16, 8]
[0, 0, 8, 4]
[0, 16, 8, 2]
[0, 2, 8, 2]

예제 입력 1 
4
2 0 4 2
4 2 2 2
2 2 2 4
2 0 4 2

3
2 2 2
4 4 4
8 8 8
예제 출력 1 
16
'''