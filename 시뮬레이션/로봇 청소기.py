'''
로봇 청소기는 다음과 같이 작동한다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    반시계 방향으로 90 회전한다.
    바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    1번으로 돌아간다.
방의 값이 0인 경우 (i, j)가 청소되지 않은 빈 칸 
방의 값이 1인 경우 (i, j)에 벽
'''
import sys
N,M = map(int, sys.stdin.readline().split())
r,c,d = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

clean_stack = [[r,c,d]]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

fire_count = 0
# d가 0인 경우 북쪽, 1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽
while True:
    x,y,dir = clean_stack.pop()
    if room[x][y] == 0: # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        room[x][y] = 2 # 2는 청소완료됨을 의미
        fire_count += 1
    while True:
        if room[x-1][y] == 0 or room[x][y+1] == 0 or room[x+1][y] == 0 or room[x][y-1] == 0: 
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
            dir = (dir + 3) % 4 # 반시계 방향으로 90 회전한다.
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            if dir == 0: # 북
                if room[x-1][y] == 0:
                    clean_stack.append([x-1,y,dir])
                    break # 1번으로 돌아간다.
            elif dir == 1: # 동
                if room[x][y+1] == 0:
                    clean_stack.append([x,y+1,dir])
                    break # 1번으로 돌아간다.
            elif dir == 2: # 남
                if room[x+1][y] == 0:
                    clean_stack.append([x+1,y,dir])
                    break # 1번으로 돌아간다.
            elif dir == 3: # 서
                if room[x][y-1] == 0:
                    clean_stack.append([x,y-1,dir])
                    break # 1번으로 돌아간다.
        else: # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            break

    if clean_stack: # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우에서 전진을 했으면
        continue # 1번으로 돌아간다.
    else: # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        if dir == 0: # 북
            if room[x+1][y] != 1:
                clean_stack.append([x+1,y,dir])
            else: # 바라보는 방향의 뒤쪽 칸이 벽(1)이라 후진할 수 없다면 작동을 멈춘다.
                break
        elif dir == 1: # 동
            if room[x][y-1] != 1:
                clean_stack.append([x,y-1,dir])
            else: # 바라보는 방향의 뒤쪽 칸이 벽(1)이라 후진할 수 없다면 작동을 멈춘다.
                break
        elif dir == 2: # 남
            if room[x-1][y] != 1:
                clean_stack.append([x-1,y,dir])
            else: # 바라보는 방향의 뒤쪽 칸이 벽(1)이라 후진할 수 없다면 작동을 멈춘다.
                break
        elif dir == 3: # 서
            if room[x][y+1] != 1:
                clean_stack.append([x,y+1,dir])
            else: # 바라보는 방향의 뒤쪽 칸이 벽(1)이라 후진할 수 없다면 작동을 멈춘다.
                break

print(fire_count)

'''
5 5
1 1 0
1 1 1 1 1
1 0 0 0 1
1 1 0 0 1
1 0 0 0 1
1
예제 입력 1 
3 3
1 1 0
1 1 1
1 0 1
1 1 1
예제 출력 1 
1
예제 입력 2
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 2 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
예제 출력 2 
57
'''