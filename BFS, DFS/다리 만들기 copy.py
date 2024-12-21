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

deque = []


def landcheck():
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
                        visit[nx][ny] = landcount


landcheck()


visit1 = []


def bridge():
    global visit1
    visit1 = [[0 for i in range(N)] for k in range(N)]
    minval = 10000000
    for i in range(N):
        for k in range(N):
            if map[i][k] == 1 and visit1[i][k] == 0:
                deque.append([i, k])
                visit1[i][k] = 1
                while len(deque) != 0:
                    pairQ = deque.pop(0)
                    for dir in range(4):
                        nx = pairQ[0] + dx[dir]
                        ny = pairQ[1] + dy[dir]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        if visit1[nx][ny] > visit1[pairQ[0]][pairQ[1]] + 1:
                            visit1[nx][ny] = visit1[pairQ[0]][pairQ[1]] + 1
                        if visit1[nx][ny] != 0:
                            continue

                        if map[nx][ny] == 1:
                            if visit[nx][ny] != 1:  # 첫번째 섬이 아닐경우
                                visit1[nx][ny] = -1
                                if visit1[pairQ[0]][pairQ[1]] < 2:
                                    continue
                                if minval > visit1[pairQ[0]][pairQ[1]]:
                                    minval = visit1[pairQ[0]][pairQ[1]]
                            else:
                                deque.append([nx, ny])
                                visit1[nx][ny] = 1
                        else:
                            deque.append([nx, ny])
                            visit1[nx][ny] = visit1[pairQ[0]][pairQ[1]] + 1
    if minval == 10000000:
        minval = 1
    return minval - 1


print(bridge())


for i in range(N):
    for k in range(N):
        print(visit1[i][k], end=" ")
    print()
