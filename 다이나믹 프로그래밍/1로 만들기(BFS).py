'''
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
'''

# BFS

import sys

N = int(sys.stdin.readline())
move = [0 for _ in range(N+1)]
move[N] = 1
from collections import deque
def BFS():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        for i in range(3):
            nx = x
            if i == 0 and x % 3 == 0: # X가 3으로 나누어 떨어지면, 3으로 나눈다.
                nx = int(nx / 3)
            elif i == 1 and x % 2 == 0: # X가 2로 나누어 떨어지면, 2로 나눈다.
                nx = int(nx / 2)
            elif i == 2: # 1을 뺀다.
                nx = nx - 1
            else:
                continue
            if move[nx] > 0:
                move[nx] = min(move[nx], move[x]+1)
            elif move[nx] == 0:
                move[nx] = move[x] + 1
            q.append(nx)
        if move[1] > 0:
            print(move[1] - 1)
            break
BFS()


'''
예제 입력 1 
2
예제 출력 1 
1
예제 입력 2 
10
예제 출력 2 
3
'''