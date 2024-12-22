# BFS 너비 우선 탐색 (Breadth-First Search)  : 다차원 배열에서 각 칸을 방문할 때 너비를 우선으로 방문하는 알고리즘
# 특정 조건에서의 최단경로 문제 해결
# 큐 자료구조 이용
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

# 파이썬식 구현
from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        print(queue, end=' ')
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        print(visited)

        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                print(i)
                queue.append(i)
                visited[i] = True

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]] 
# 그래프 문제는 보통 노드의 번호가 1번부터 시작하는 경우가 많아 인덱스 0은 비워둠
# 1번 노드와는 [2,3,8]이 연결되어 있음
# 2번 노드와는 [1,7]이 연결되어 있음
# 3번 노드와는 [1,4,5]가 연결되어 있음
# ...

visited = [False]*len(graph)

bfs(graph, 1, visited)


# c 구현(바킹독)
'''
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x = 4
y = 6

board = [[0 for i in range(x)] for k in range(y)]
vis = [[0 for i in range(x)] for k in range(y)]

from collections import deque

listQ = deque()


def BFS(x, y):
    vis[0][0] = 1
    listQ.append([0, 0])
    while len(listQ) != 0:
        curlist = listQ[0]  # front => (맨앞의 값 가져오기)
        listQ.popleft()  # BFS는 FIFO인 큐를 사용함 => popleft(맨앞의 값 빼기)
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
'''