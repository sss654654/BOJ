'''
입력
첫째 줄에 노트북의 세로와 가로 길이를 나타내는 N(1 ≤ N ≤ 40)과 M(1 ≤ M ≤ 40), 
그리고 스티커의 개수 K(1 ≤ K ≤ 100)이 한 칸의 빈칸을 사이에 두고 주어진다.

그 다음 줄부터는 K개의 스티커들에 대한 정보가 주어진다. 각 스티커는 아래와 같은 형식으로 주어진다.

먼저 i번째 스티커가 인쇄된 모눈종이의 행의 개수와 열의 개수를 나타내는 
Ri(1 ≤ Ri ≤ 10)와 Ci(1 ≤ Ci ≤ 10)가 한 칸의 빈칸을 사이에 두고 주어진다.

다음 Ri개의 줄에는 각 줄마다 모눈종이의 각 행을 나타내는 Ci개의 정수가 한 개의 빈칸을 사이에 두고 주어진다. 
각 칸에 들어가는 값은 0, 1이다. 0은 스티커가 붙지 않은 칸을, 1은 스티커가 붙은 칸을 의미한다.

문제에서 설명한 것과 같이 스티커는 모두 올바른 모눈종이에 인쇄되어 있다. 
구체적으로 스티커의 각 칸은 상하좌우로 모두 연결되어 있고, 
모눈종이의 크기는 스티커의 크기에 꼭 맞아서 상하좌우에 스티커에 전혀 포함되지 않는 불필요한 행이나 열이 존재하지 않는다.

출력
첫째 줄에 주어진 스티커들을 차례대로 붙였을 때 노트북에서 스티커가 붙은 칸의 수를 출력한다.
'''

import sys
from collections import deque
N,M,K = map(int, sys.stdin.readline().split())
st_stack = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(i,j):
    q = deque()
    q.append([i,j])
    is_visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = dx[dir] + x
            ny = dy[dir] + y
            if nx<0 or nx>=R or ny<0 or ny >=C:
                continue
            if tmp_stack[nx][ny] == 0 or is_visited[nx][ny] == 1:
                continue
            q.append([nx,ny])
            is_visited[nx][ny] = 1

for i in range(K):
    R, C = map(int, sys.stdin.readline().split())
    tmp_stack = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
    is_visited = [[0 for _ in range(C)] for _ in range(R)]
    
    # 스티커는 상하좌우에 불필요한 행이 존재하면 안되며, 스티커는 연결되어있어야 함
    dont_push = 0
    for t in tmp_stack: # 가로 행(0,0,0) 체크
        if sum(t) == 0:
            dont_push = 1
            break
    for i in range(C): # 세로 행(0,0,0) 체크
        check = 0
        for j in range(R):
            check += tmp_stack[j][i]
        if check == 0:
            dont_push = 1
    check = 0
    for i in range(R): # bfs로 떨어져있는 스티커 체크
        for j in range(C):
            if tmp_stack[i][j] == 1 and is_visited[i][j] == 0:
                check += 1
                BFS(i,j)
    if check > 1:
        dont_push = 1

    if not dont_push:
        st_stack.append(tmp_stack)

# N(세로), M(가로)
notebook = [[0 for _ in range(M)] for _ in range(N)]

def rotate(list): # 인자로 받은 리스트를 90도 돌려서 반환하는 함수
    x = len(list) # 2
    y = len(list[0]) # 3
    result = []
    for i in range(y):
        tmp = []
        for j in range(x-1,-1,-1):
            tmp.append(list[j][i])
        result.append(tmp)
    return result
'''
ex) [[1,1,1],[1,0,1]]([2][3]) -> [[1,1],[0,1],[1,1]]([3][2]) -> [[1,0,1],[1,1,1]] ->[[1,1][1,0][1,1]]

(2,3)
[0,0][0,1][0,2](1,1,1)
[1,0][1,1][1,2](1,0,1)
->
(3,2)
[1,0][0,0](1,1)
[1,1][0,1](0,1)
[1,2][0,2](1,1)
->
(2,3)
[1,2][1,1][1,0](1,0,1)
[0,2][0,1][0,0](1,1,1)
'''

# 스티커 스택에 대한 반복문으로 시작해 일단
# 스티커가 노트북에 붙일 수 있는지 확인은 어떻게하지? bfs로 0만 탐색?

'''
1. 스티커를 회전시키지 않고 모눈종이에서 떼어낸다.
2. 다른 스티커와 겹치거나 노트북을 벗어나지 않으면서 스티커를 붙일 수 있는 위치를 찾는다. 
혜윤이는 노트북의 위쪽부터 스티커를 채워 나가려고 해서, 스티커를 붙일 수 있는 위치가 여러 곳 있다면 가장 위쪽의 위치를 선택한다. 
가장 위쪽에 해당하는 위치도 여러 곳이 있다면 그중에서 가장 왼쪽의 위치를 선택한다.
3. 선택한 위치에 스티커를 붙인다. 
만약 스티커를 붙일 수 있는 위치가 전혀 없어서 스티커를 붙이지 못했다면, 스티커를 시계 방향으로 90도 회전한 뒤 2번 과정을 반복한다.
4. 위의 과정을 네 번 반복해서 스티커를 0도, 90도, 180도, 270도 회전시켜 봤음에도 스티커를 붙이지 못했다면 
해당 스티커를 붙이지 않고 버린다.
'''

def is_possible(st,x_s,x_f,y_s,y_f): #(st,0,5,0,1) - (st,0,5,1,2) - (st,0,5,2,3)
    for i in range(x_s,x_f):
        for j in range(y_s,y_f):
            if notebook[i][j] == 1 and st[i-x_s][j-y_s] == 1: # 붙이려는 노트북에 이미 스티커가 존재할 경우
                return False
    return True

for st in st_stack:
    rotate_count = 0
    while True: # notebook의 x=5, y=4
        if rotate_count == 4: # 0도, 90도, 180도, 270도를 확인한 후 다시 원상태(360)로 돌아올 경우 while 탈출
            break
        # 스티커의 x=2, y=5 -rotate-> x=5, y=2
        # 즉, x=5,y=2 스티커는, x=5,y=4 노트북의 y=0~1 / y=1~2 / y=2~3 에 붙일 수 있다!
        x_len = len(st) # 스티커의 x축 길이
        y_len = len(st[0]) # 스티커의 y축 길이
        if x_len > N or y_len > M: # 스티커의 x축이나 y축의 길이가 노트북의 길이를 벗어날 경우
            rotate_count += 1
            st = rotate(st) # 90(1) 180(2) 270(3)
            continue
        # N(x), M(y) / x_len, y_len
        # N이 5고 x_len이 1이면 5가지의 경우의 수
        # N이 5고 x_len이 2이면 4가지의 경우의 수
        # N이 5고 x_len이 3이면 3가지의 경우의 수
        # N이 5고 x_len이 4이면 2가지의 경우의 수
        # N이 5고 x_len이 5이면 1가지의 경우의 수
        # 즉 X,Y 변수에 경우의 수를 담아 반복문을 돌리면 됨
        # ex) N=5,M=4 / x_len=5,y_len=2
        X = N - x_len + 1 # 5 - 5 + 1 = 1개
        Y = M - y_len + 1 # 4 - 2 + 1 = 3개

        put_st = 0 # False
        for i in range(X): # x가 가진 경우의 수
            for j in range(Y): # y가 가진 경우의 수
                put_st = is_possible(st,i,i+x_len,j,j+y_len)
                if put_st: # is_possible을 통해 True를 받았을 경우
                    for k in range(i,i+x_len): # 왼쪽 위부터
                        for l in range(j,j+y_len): # 오른쪽으로 진행
                            if st[k-i][l-j] == 1: # 스티커는 떼서 붙이는 것!
                                # 이 조건문이 없으면 0꺼지 붙여지게됨
                                notebook[k][l] = st[k-i][l-j]
                    break # 노트북에 다 붙였으면 이중 반복문 탈출
            if put_st: # 이중 반복문이므로 한번더 break
                break

        if put_st: # 스티커가 노트북에 붙여졌으면 다음 스티커로 넘어가기 위해 while 빠져나가기
            break
        else: # 스티커가 못 붙여졌으면 회전 횟수 +1한 후 스티커 회전(rotate())
            rotate_count += 1
            st = rotate(st) # 90(1) 180(2) 270(3)

result = 0
for i in range(N):
    for j in range(M):
        if notebook[i][j] == 1: # 노트북에 붙여진 스티커부분의 개수 세기
            result += 1
print(result)


# 직면한 과제
# 1. 스티커를 90도로 돌려 -> rotate(list)
# 2. 노트북의 왼쪽 위부터 빈자리를 찾아서 st_stack에 담긴 스티커들을 붙여야 함 -> 반복문? bfs?

'''
예제 입력 1 
5 4 4
3 3
1 0 1
1 1 1
1 0 1
2 5
1 1 1 1 1
0 0 0 1 0
2 3
1 1 1
1 0 1
3 3
1 0 0
1 1 1
1 0 0
예제 출력 1 
18
예제 입력 2 
1 3 3
2 3
1 0 0
1 1 1
1 1
1
3 1
1
1
1
예제 출력 2 
1
예제 입력 3 
2 3 3
2 3
1 1 1
1 0 0
2 1
1
1
2 2
1 0
1 1
예제 출력 3 
6
예제 입력 4 
4 5 4
3 3
1 0 1
1 1 1
0 1 0
2 4
1 1 1 1
0 1 0 1
1 4
1 1 1 1
4 2
1 0
1 1
0 1
0 1
예제 출력 4 
17
예제 입력 5 
2 2 3
3 1
1
1
1
2 3
1 0 1
1 1 1
2 4
1 0 1 1
1 1 1 0
예제 출력 5 
0
예제 입력 6 
6 7 5
4 6
1 0 0 1 0 1
1 1 0 1 0 1
1 1 1 1 1 1
0 0 0 1 0 0
4 3
0 1 0
1 1 1
0 1 1
1 1 0
3 6
1 1 1 1 1 1
0 0 1 0 0 0
0 0 1 0 0 0
6 6
0 0 1 1 0 0
1 1 1 1 0 1
0 0 1 1 1 1
0 0 1 1 1 1
1 1 1 0 1 1
0 1 0 0 1 0
4 4
1 1 1 1
0 0 0 1
0 0 1 1
0 0 0 1
예제 출력 6 
30
예제 입력 7 
6 8 3
4 5
0 0 1 1 1
1 1 1 0 1
0 0 1 0 1
0 0 1 0 0
5 4
0 0 1 0
1 1 1 1
1 1 0 1
1 1 0 0
1 1 0 0
5 6
0 0 1 1 1 1
1 1 1 1 0 0
1 1 1 1 1 0
0 1 0 1 0 0
0 1 0 1 0 0
예제 출력 7 
22
예제 입력 8 
8 6 6
3 5
0 1 0 0 0
1 1 1 1 1
0 1 0 0 1
6 3
0 0 1
0 0 1
0 0 1
1 1 1
1 0 1
1 1 1
6 3
1 1 0
1 0 0
1 1 1
1 0 1
1 0 0
1 0 0
6 6
0 0 0 0 1 0
0 0 1 0 1 0
0 0 1 0 1 0
0 1 1 1 1 0
0 1 1 0 1 1
1 1 1 0 0 0
4 5
0 0 0 0 1
1 0 0 1 1
1 1 1 1 0
1 1 0 1 0
4 3
1 1 0
1 0 0
1 1 1
1 1 1
예제 출력 8 
29
'''