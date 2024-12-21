# DFS 깊이 우선 탐색 (Depth-First Search) : 다차원 배열에서 각 칸을 방문할 때 깊이를 우선으로 방문하는 알고리즘

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


board = [[0 for i in range(4)] for k in range(4)]
visit = [[0 for i in range(4)] for k in range(4)]

stack = []


def DFS(x, y):
    visit[0][0] = 1
    stack.append([0, 0])

    while len(stack) != 0:  # stack이 비면 끝
        curlist = stack.pop()
        print("( {},{} ) -> ".format(curlist[0], curlist[1]), end="")
        # x, y
        for dir in range(4):
            curx = dx[dir] + curlist[0]
            cury = dy[dir] + curlist[1]
            if curx < 0 or curx >= x or cury < 0 or cury >= y:
                # 보드의 왼쪽(0미만), 오른쪽(정한 크기 x 이상) 일 경우 [x]

                continue
            if board[curx][cury] == 1 or visit[curx][cury] == 1:
                # 방문하면 안되는 곳이거나 방문을 이미 했거나
                continue
            visit[curx][cury] = 1
            stack.append([curx, cury])


DFS(4, 4)
