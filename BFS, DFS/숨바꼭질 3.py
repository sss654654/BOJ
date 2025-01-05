'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
'''
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

dx = [2,-1,1]
visited = [0 for i in range(100001)]
def BFS():
    global result
    q = deque()
    q.append(N)
    visited[N] = 1
    while q:
        x = q.popleft()
        if x == K:
            print(visited[x]-1)
            break
        for dir in range(3):
            nx = 0
            if dir == 0:
            # 먼저 순간이동을 체크하지 않으면 '1 2'의 경우 순간이동으로 찾을 수 있음에도 걸어서 찾아
            # 답이 0이 아닌 1이 되게 됨
                nx = x * dx[dir]
            elif dir == 1:
                nx = x + dx[dir]
            else:
                nx = x + dx[dir]
            if nx<0 or nx>100000:
                continue
            if visited[nx] != 0:
                continue
            if dx[dir] != 2:
                visited[nx] = visited[x] + 1
            else:
                visited[nx] = visited[x]
            q.append(nx)
BFS()
#print(visited[:100])
'''
예제 입력 1 
5 17
예제 출력 1 
2
힌트
수빈이가 5-10-9-18-17 순으로 가면 2초만에 동생을 찾을 수 있다.
'''