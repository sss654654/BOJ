# BFS 너비 우선 탐색 (Breadth-First Search)  : 다차원 배열에서 각 칸을 방문할 때 너비를 우선으로 방문하는 알고리즘

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x = 4
y = 6

board = [[0 for i in range(x)] for k in range(y)]
vis = [[0 for i in range(x)] for k in range(y)]

listQ = []


def BFS(x, y):
    vis[0][0] = 1
    listQ.append([0, 0])
    while len(listQ) != 0:
        curlist = listQ[0]  # front => (맨앞의 값 가져오기)
        listQ.pop(0)  # BFS는 FIFO인 큐를 사용함 => pop(맨앞의 값 빼기)
        print("( {},{} ) -> ".format(curlist[0], curlist[1]), end="")
        for dir in range(4):
            nx = curlist[0] + dx[dir]
            ny = curlist[1] + dy[dir]
            if nx < 0 or nx >= x or ny < 0 or ny >= y:
                continue
            if vis[nx][ny] == 1 or board[nx][ny] == 1:
                continue
            vis[nx][ny] = 1
            listQ.append([nx, ny])


BFS(4, 4)
