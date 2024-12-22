# DFS 깊이 우선 탐색 (Depth-First Search) : 다차원 배열에서 각 칸을 방문할 때 깊이를 우선으로 방문하는 알고리즘
# 스택 혹은 재귀 함수를 이용
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리.
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

# 파이썬식 구현

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True 
    print(v, end=' ')
    print(visited)

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]] 
# 그래프 문제는 보통 노드의 번호가 1번부터 시작하는 경우가 많아 인덱스 0은 비워둠
# 1번 노드와는 [2,3,8]이 연결되어 있음
# 2번 노드와는 [1,7]이 연결되어 있음
# 3번 노드와는 [1,4,5]가 연결되어 있음
# ...

visited = [False]*len(graph)

dfs(graph, 1, visited)


# c 구현(바킹독)
'''
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
'''