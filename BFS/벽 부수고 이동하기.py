M, N = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

miro = [[0 for i in range(N)] for k in range(M)]
visit = [[[0 for i in range(2)] for k in range(N)] for j in range(M)]
# visit = [방문거리, 벽 부순세계(1) / 부수지 않은 세계(0)]

# M = Y, N = X

for col in range(M):
    Nstr = input()
    rowindex = 0
    for row in Nstr:
        miro[col][rowindex] = int(row)
        rowindex += 1


def BFS():
    queue = []
    queue.append([0, 0, 0])
    visit[0][0][0] = 1
    while len(queue) != 0:  # queue가 빌 경우
        pairQ = queue.pop(0)

        if pairQ[0] == M-1 and pairQ[1] == N-1:
            return visit[pairQ[0]][pairQ[1]][pairQ[2]]

        for dir in range(4):
            nx = dx[dir] + pairQ[0]
            ny = dy[dir] + pairQ[1]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            # N = Y, M = X
            # 벽을 부순 세계 pairQ[2] = 1
            # 벽을 아직 부수지 않은 세계로 나누어야 함 pairQ[2] = 0
            if visit[nx][ny][pairQ[2]] != 0:
                # visit[0] 0이 아니면 방문하여 찍은 것
                continue
            if miro[nx][ny] == 0:
                # 미로가 막혀있지 않을 경우
                visit[nx][ny][pairQ[2]] = visit[pairQ[0]
                                                ][pairQ[1]][pairQ[2]] + 1
                queue.append([nx, ny, pairQ[2]])
            if miro[nx][ny] == 1 and pairQ[2] == 0:
                # 미로가 막혀있고 벽을 부순적이 없는 경우
                visit[nx][ny][1] = visit[pairQ[0]][pairQ[1]][pairQ[2]] + 1
                queue.append([nx, ny, 1])
    return -1


print(BFS())
