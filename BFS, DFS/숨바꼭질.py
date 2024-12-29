'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 

수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
'''

import sys
# n은 수빈, k는 동생 / n(수빈)은 앞(+1), 뒤(-1), 순간이동(2n) 가능
N, K = map(int, sys.stdin.readline().split())

find = [-1 for i in range(100001)]

from collections import deque

def bfs(N,K):
    find[N] = 0
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        for dir in range(3):
            dx = 0
            if dir == 0:
                dx = x + 1
            elif dir == 1:
                dx = x - 1
            else:
                dx = x * 2
            if dx < 0 or dx >= 100001:
                continue
            if find[dx] != -1:
                continue
            find[dx] = find[x] + 1
            q.append(dx)
        if find[K] != -1:
            print(find[K])
            break
bfs(N,K)

'''
예제 입력 1 
5 17
예제 출력 1 
4
'''