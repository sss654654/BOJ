import sys
from collections import deque

#    [하,우,상,좌]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def check(x,y):
    return x<0 or x>=N or y<0 or y>=M

def update(x,y,dir): # [x,y]에서 dir 방향으로 진행하면서 벽을 만날 때 까지 지차니는 모든 빈 칸을 7로 변경
    # 1234를 1,2,3,4로 빼려면 %10과 /10을 반복(10진법)
    # 4진법은 %4와 /4를 반복

    # dir = 0 [1,0] 하 / dir = 1 [0,1] 우 / dir = 2 [-1,0] 상 / dir = 3 [0,-1] 좌
    dir = dir % 4 # dir과 dir+2가 넘어오는 경우는 cctv2인 것 -> (상,하) / (좌,우)
    while True:
        x += dx[dir]
        y += dy[dir]
        if check(x,y) or cctv_view[x][y] == 6: # cctv가 맵을 벗어나거나, 움직인 곳이 벽일 경우
            return
        if cctv_view[x][y] != 0: # 움직인 칸에 cctv가 있을 경우
            continue
        cctv_view[x][y] = 7 # cctv가 본 곳을 cctv의 번호(1,2,3,4,5)와 벽(6)을 제외한 숫자로 체크

N, M = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cctv_view = [[0 for _ in range(M)] for _ in range(N)]
cctv_stack = deque() # cctv의 좌표를 담을 스택

for i in range(N):
    for j in range(M):
        if room[i][j] != 0 and room[i][j] != 6: # cctv(1~5)
            cctv_stack.append([i,j])

# cctv들의 방향 설정
# cctv가 k개 있다고 할 때 tmp는 0부터 4^k - 1까지 돌아야 함
# cctv1,3,4는 가짓 수가 네개이나 cctv2는 두 개이고 cctv5는 한 개임(중복되도 그냥 무시하고 진행)
mn = sys.maxsize
for tmp in range(4**len(cctv_stack)): # cctv가 3개면 0~63(64)
    for i in range(N):
        for j in range(M):
            # 초기화 why? -> 아래에서 cctv가 본 곳은 update함수를 통해 7로 뒤덮었기 때문
            cctv_view[i][j] = room[i][j]

    brute = tmp # brute = 0~63
    for i in range(len(cctv_stack)): # 각 cctv가 자신의 번호(1,2,3,4,5)에 맞게 움직임
        dir = brute % 4 # 나머지 -> 움직일 거리(0,1,2,3 반복)
        brute = int(brute / 4) # brute를 4진법으로 해체 -> 이는 각 cctv가 다르게 움직이게 하기 위함(4x4x4)
        # ex) cctv개수가 3개고 brute가 21이었을 경우
        # 첫번 째 cctv의 dir(21%4) = 1
        # 두번 째 cctv의 dir((21/4)%4)=(5%4) = 1
        # 세번 째 cctv의 dir((5/4)%4)=(1%4) = 1

        # 각 cctv의 좌표를 x,y에 저장
        x = cctv_stack[i][0]
        y = cctv_stack[i][1]
        if room[x][y] == 1:
            update(x,y,dir) # 현재 cctv의 좌표와 cctv1이 볼 방향(dir) 4가지 중 하나를 넘김
        elif room[x][y] == 2:
            update(x,y,dir) # 하, 우, 상, 좌
            update(x,y,dir+2) # 상, 좌, 하, 우 -> update에도 %4가 있기 때문에 cctv2의 특징(상하, 좌우) 구현 가능
        elif room[x][y] == 3: # ㄴ자로 돌기 때문에 dir과 dir+1
            update(x,y,dir)
            update(x,y,dir+1)
        elif room[x][y] == 4: # ㅗ자로 세 방면을 바라보며 돌기 때문에 dir, dir+1, dir+2
            update(x,y,dir)
            update(x,y,dir+1)
            update(x,y,dir+2)
        else:
            update(x,y,dir)
            update(x,y,dir+1)
            update(x,y,dir+2)
            update(x,y,dir+3)
        val = 0
        for i in range(N):
            for j in range(M):
                val += (cctv_view[i][j] == 0) # 사각지대(0)면 True(1)반환하므로 val에 더해 최솟값 구하기
        mn = min(mn,val)
print(mn)

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