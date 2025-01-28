'''

입력
첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 

CCTV의 최대 개수는 8개를 넘지 않는다.

출력
첫째 줄에 사각 지대의 최소 크기를 출력한다.
'''
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cctv_view = [[0 for _ in range(M)] for _ in range(N)]
# 각각의 cctv가 볼 수 있는 가능성의 수를 모두 따져보면서 그에대한 방문하지 않은 곳(0)의 수를 세야함
# bfs? 백트래킹?
# 1의 가짓 수(4) 2의 가짓 수(2) 3의 가짓 수(4) 4의 가짓 수(4) 5의 가짓 수(1)
# cctv는 8개 까지니까 만약 1,3,4 종류로 8개인 경우 4^8의 가짓 수에 대해서 사각 지대의 최소 크기를 구해야 돼
# 백트래킹을 써서 가지를 뻗어나가 최솟 값을 계속 구해 근데 이러면 모든 가짓수를 다 체크해야되네?

cctv_stack = deque()
cctv_count = 0
for i in range(N):
    for j in range(M):
        if room[i][j] != 0 and room[i][j] != 6:
            cctv_stack.append([i,j,room[i][j]])
cctv_count = len(cctv_stack)
min_val = sys.maxsize

def non_cctv_view_count():
    result = 0
    for i in range(N):
        for j in range(M):
            if cctv_view[i][j] == 0 and room[i][j] != 6:
                result += 1
    return result

def cctv_view_clear():
    for i in range(N):
        for j in range(M):
            cctv_view[i][j] = 0

def left_check(x,y):
    for i in range(y, 0-1, -1): # 왼쪽 사각지대 탐색
            if room[x][i] == 6:
                break
            cctv_view[x][i] += 1
def right_check(x,y):
    for i in range(y, M): # 오른쪽 사각지대 탐색
            if room[x][i] == 6: # 벽이면 칠하고 벗어나기
                break
            cctv_view[x][i] += 1 # cctv가 본 곳은 자취 남기기(+1)
def up_check(x,y):
    for i in range(x, 0-1, -1): # 위쪽 사각지대 탐색
            if room[i][y] == 6:
                break
            cctv_view[i][y] += 1
def down_check(x,y):
    for i in range(x, N): # 아래쪽 사각지대 탐색
            if room[i][y] == 6:
                break
            cctv_view[i][y] += 1

def left_rollback(x,y):
    for i in range(y, 0-1, -1): # 왼쪽 사각지대 롤백
            if room[x][i] == 6:
                break
            cctv_view[x][i] -= 1
def right_rollback(x,y):
    for i in range(y, M): # 오른쪽 사각지대 롤백
            if room[x][i] == 6:
                break
            cctv_view[x][i] -= 1 # cctv가 본 곳 회수
def up_rollback(x,y):
    for i in range(x, 0-1, -1): # 위쪽 사각지대 롤백
            if room[i][y] == 6:
                break
            cctv_view[i][y] -= 1
def down_rollback(x,y):
    for i in range(x, N): # 아래쪽 사각지대 롤백
            if room[i][y] == 6:
                break
            cctv_view[i][y] -= 1


def cctv(k):
    global min_val
    if k == cctv_count:
        view_count = non_cctv_view_count()
        if min_val > view_count:
            min_val = view_count
            '''
            print(min_val)
            for i in range(N):
                print(cctv_view[i])
            '''
        return
    
    x = cctv_stack[k][0]
    y = cctv_stack[k][1]
    cctv_num = cctv_stack[k][2]

    if cctv_num == 1:
        # 이론적으론 맞는 것 같아
        # 뭘 해야되냐 그럼 칠한것을 다시 롤백해야돼

        right_check(x,y)
        cctv(k+1)
        right_rollback(x,y)

        down_check(x,y)
        cctv(k+1)
        down_rollback(x,y)

        left_check(x,y)
        cctv(k+1)
        left_rollback(x,y)
    

        up_check(x,y)
        cctv(k+1)
        up_rollback(x,y)

        return # cctv1이 볼 수 있는 사각을 다 보았을 경우 돌아가
    elif cctv_num == 2:

        # 좌/우 탐색
        left_check(x,y)
        right_check(x,y)
        cctv(k+1)
        left_rollback(x,y)
        right_rollback(x,y)
        
        # 상/하 탐색
        up_check(x,y)
        down_check(x,y)
        cctv(k+1)
        up_rollback(x,y)
        down_rollback(x,y)

        return
    elif cctv_num == 3:
        up_check(x,y)
        right_check(x,y)
        cctv(k+1)
        up_rollback(x,y)
        right_rollback(x,y)

        right_check(x,y)
        down_check(x,y)
        cctv(k+1)
        right_rollback(x,y)
        down_rollback(x,y)

        left_check(x,y)
        down_check(x,y)
        cctv(k+1)
        left_rollback(x,y)
        down_rollback(x,y)

        left_check(x,y)
        up_check(x,y)
        cctv(k+1)
        left_rollback(x,y)
        up_rollback(x,y)

        return
    elif cctv_num == 4:
        up_check(x,y)
        right_check(x,y)
        down_check(x,y)
        cctv(k+1)
        up_rollback(x,y)
        right_rollback(x,y)
        down_rollback(x,y)

        left_check(x,y)
        right_check(x,y)
        down_check(x,y)
        cctv(k+1)
        left_rollback(x,y)
        right_rollback(x,y)
        down_rollback(x,y)

        left_check(x,y)
        up_check(x,y)
        down_check(x,y)
        cctv(k+1)
        left_rollback(x,y)
        up_rollback(x,y)
        down_rollback(x,y)

        left_check(x,y)
        up_check(x,y)
        right_check(x,y)
        cctv(k+1)
        left_rollback(x,y)
        up_rollback(x,y)
        right_rollback(x,y)

        return
    elif cctv_num == 5:
        # 상/하/좌/우 탐색.
        up_check(x,y)
        down_check(x,y)
        left_check(x,y)
        right_check(x,y)
        cctv(k+1)
        up_rollback(x,y)
        down_rollback(x,y)
        left_rollback(x,y)
        right_rollback(x,y)

        return
    
cctv(0)
print(min_val)
'''
6 6
1 0 0 0 0 0
0 2 0 0 0 0
0 0 3 0 0 0
0 0 0 4 0 0
0 0 0 0 5 0
0 0 0 0 0 6
# 답 : 4

3 3
0 0 0
0 5 0
0 0 0
# 답 : 4

4 5
0 0 2 0 3
0 6 0 0 0
0 0 6 6 0
0 0 0 0 0
# 답 : 8

1 1
0
# 답 : 1

6 6
0 0 0 0 0 0
0 0 4 0 0 0
0 4 2 0 4 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 4 0 0 0
# 답 : 9

1 7
0 3 0 0 3 0 0
# 답 : 0

5 5
0 0 0 0 0
6 2 0 0 4
0 0 0 4 0
5 0 0 5 0
6 0 0 0 0
# 답 : 3

3 3
0 0 0
0 4 0
0 0 0
# 답 : 5

5 2
0 0
0 0
3 0
0 0
6 0
# 답 : 5

3 3
6 6 6
6 6 6
0 6 6
# 답 : 1

5 5
5 1 6 1 4
6 0 1 6 3
2 5 0 0 0
0 6 0 0 0
6 0 6 6 6
# 답 : 2

3 1
5
6
0
# 답 : 1

----------------------

5 5
6 0 6 6 0
6 4 2 0 0
2 6 0 4 6
6 6 0 6 6
0 0 0 6 6
# 답 : 3

4 6
2 6 0 3 0 2
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 6 1
# 답 : 8

5 5
0 0 0 0 0
6 2 0 0 4
0 0 0 4 0
5 0 0 5 0
6 0 0 0 0
# 답 : 3

6 5
2 2 6 0 5
0 6 6 0 4
6 6 0 0 0
2 6 4 6 0
6 3 0 0 6
6 4 0 6 6
# 답 : 1

5 6
0 3 0 0 0 0
0 0 0 0 0 0
6 0 0 2 2 0
6 1 2 0 6 6
0 0 6 0 6 6
# 답 : 5

4 5
0 0 0 6 0
6 0 6 0 0
2 6 0 0 0
0 0 6 0 3
# 답 : 8

4 4
0 4 0 2
0 0 0 2
0 0 0 0
3 5 0 0
# 답 : 1

5 5
2 0 6 3 4
0 0 6 0 0
0 0 6 0 5
6 0 3 4 2
0 5 0 0 0
# 답 : 0

3 6
0 5 5 0 2 0
0 0 2 0 0 3
0 0 0 0 0 0
# 답 : 2

5 4
6 6 6 6
6 0 6 6
6 2 6 0
6 0 6 6
6 6 6 6
# 답 : 1

4 5
0 6 0 6 4
6 6 6 0 0
0 0 6 3 4
0 6 0 0 0
# 답 : 7

4 3
0 0 0
3 0 0
0 2 2
0 1 6
# 답 : 1
    
5 5
1 4 0 5 0
0 0 0 0 0
4 0 0 0 3
5 6 3 0 0
0 0 0 0 0
# 답 : 3

5 3
0 6 6
1 0 0
6 0 0
6 6 3
0 0 0
# 답 : 5

5 5
6 6 6 6 6
6 0 6 3 0
0 0 0 0 6
6 6 0 6 2
0 0 2 6 0
# 답 : 5

3 3
3 0 0
0 0 0
0 0 0
# 답 : 4

3 3
6 6 6
6 6 6
0 6 6
# 답 : 1

1 6
0 6 5 6 0 0
# 답 : 3

3 1
6
5
0
# 답 : 0

3 3
0 5 0
6 0 0
6 0 0
# 답 : 2

3 3
6 0 0
0 3 0
5 0 6
# 답 : 1

2 3
0 2 6
5 0 0
# 답 : 0

2 3
5 0 4
0 6 1
# 답 : 0

8 8
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
# 답 : 64

2 4
1 1 0 5
0 0 0 0
# 답 : 1

8 8
0 0 0 0 0 0 0 1
0 0 0 0 0 0 1 0
0 0 0 1 0 0 0 0
0 0 0 0 0 1 0 0
1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0
0 1 0 0 0 0 0 0
# 답 : 12

7 5
0 6 6 6 6
6 0 6 4 6
6 6 1 2 6
6 0 1 6 0
6 6 0 0 6
0 6 0 6 6
3 0 6 0 0
# 답 : 6

1 5
0 5 6 0 0
# 답 : 2

8 8
6 6 6 6 6 6 6 6
6 6 6 6 6 6 6 6
6 6 6 6 6 6 6 6
6 6 6 6 6 6 6 6
6 6 6 6 6 6 6 6
6 6 6 6 6 6 6 6
6 6 6 6 6 6 6 6
6 6 6 6 6 6 6 6
6 6 6 6 6 6 6 6
# 답 : 0 
'''

'''
예제 입력 1 
4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
예제 출력 1 
20
예제 입력 2 
6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
예제 출력 2 
15
예제 입력 3 
6 6
1 0 0 0 0 0
0 1 0 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 0 0 1
예제 출력 3 
6
예제 입력 4 
6 6
1 0 0 0 0 0
0 1 0 0 0 0
0 0 1 5 0 0
0 0 5 1 0 0
0 0 0 0 1 0
0 0 0 0 0 1
예제 출력 4 
2
예제 입력 5 
1 7
0 1 2 3 4 5 6
예제 출력 5 
0
예제 입력 6 
3 7
4 0 0 0 0 0 0
0 0 0 2 0 0 0
0 0 0 0 0 0 4
예제 출력 6 
0

'''