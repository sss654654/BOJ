import sys
N = int(input())

map = []
visit = [[0 for i in range(N)] for k in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


T = N

while T != 0:
    if T < 0:
        break
    T -= 1
    map.append([int(x) for x in input().split()])


def landcheck():
    deque = []
    landcount = 0
    for i in range(N):
        for k in range(N):
            if map[i][k] == 1 and visit[i][k] == 0:
                landcount += 1
                deque.append([i, k])
                visit[i][k] = landcount
                while len(deque) != 0:
                    pairQ = deque.pop(0)
                    for dir in range(4):
                        nx = pairQ[0] + dx[dir]
                        ny = pairQ[1] + dy[dir]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        if visit[nx][ny] > 0 or map[nx][ny] == 0:
                            continue
                        deque.append([nx, ny])
                        visit[nx][ny] = landcount  # 섬에 번호부여
    return landcount


landcount = landcheck()


minval = sys.maxsize

visit1 = []


def bridge(Ncount):
    global visit1
    global minval
    deque = []
    
    visit1 = [[-1]*N for k in range(N)]
    for i in range(N):
        for k in range(N):
            if visit[i][k] == Ncount:
                deque.append([i, k])
                visit1[i][k] = 0
    while len(deque) != 0:
        pairQ = deque.pop(0)
        for dir in range(4):
            nx = pairQ[0] + dx[dir]
            ny = pairQ[1] + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visit[nx][ny] == 0 and visit1[nx][ny] == -1:  # 바다
                visit1[nx][ny] = visit1[pairQ[0]][pairQ[1]] + 1
                deque.append([nx, ny])
            if visit[nx][ny] != 0 and visit[nx][ny] != Ncount:  # 지정된 섬과 다른 섬
                if minval > visit1[pairQ[0]][pairQ[1]]:
                    minval = visit1[pairQ[0]][pairQ[1]]
                    return


for i in range(1, landcount+1):
    bridge(i)

print(minval)
