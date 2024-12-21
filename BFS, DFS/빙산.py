import sys
from collections import deque

Y, X = map(int, input().split())
# (5,7)
ice = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = Y

while T != 0:
    if T < 0:
        break
    T -= 1
    ice.append([int(x) for x in input().split()])

# 7(X)행 5(Y)열


def MeltIce():
    queue = deque()
    icecount = 0
    visit = [[0 for i in range(X)] for k in range(Y)]
    for i in range(Y):  # 5
        for j in range(X):  # 7
            if ice[i][j] != 0 and visit[i][j] == 0:
                icecount += 1  # 따로 떨어진 빙산 체크
                queue.append((i, j))
                visit[i][j] = 1
                while queue:  # 빙산 하나의 1년
                    pairY, pairX = queue.popleft()
                    meltcount = 0
                    for dir in range(4):
                        ny = pairY + dy[dir]
                        nx = pairX + dx[dir]
                        # Y = 5, X = 7
                        if ny < 0 or ny >= Y or nx < 0 or nx >= X:
                            continue
                        if visit[ny][nx] > 0:
                            continue
                        if ice[ny][nx] == 0 and visit[ny][nx] != 1:
                            meltcount += 1
                            continue
                        queue.append((ny, nx))
                        visit[ny][nx] = 1
                    ice[pairY][pairX] = ice[pairY][pairX] - meltcount
                    if ice[pairY][pairX] < 0:
                        ice[pairY][pairX] = 0
                        '''
                print()
                for i in range(Y):
                    for k in range(X):
                        print(ice[i][k], end=" ")
                    print()
                    '''

    return icecount


year = 0
while True:
    icecount = MeltIce()
    if icecount > 1:
        break
    elif icecount == 0:
        year = 0
        break
    year += 1

print(year)
