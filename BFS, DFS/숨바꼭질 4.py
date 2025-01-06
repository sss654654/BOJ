'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.
'''
import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
visited = []
result_val = 0
result_list = []
dx = [[2,1,-1], [1,-1,2]]
def BFS():
    global result_val
    q = deque()
    for d in dx:
        visited = [0 for i in range(100001)]
        q.append([N])
        visited[N] = 1
        while q:
            x_list = q.popleft()
            x = x_list[-1]
            if x == K:
                result_val = visited[x] - 1
                result_list.append(x_list)
            for dir in d:
                nx = 0
                if dir == 2:
                    nx = x*dir
                else:
                    nx = x+dir
                if nx<0 or nx>=100000:
                    continue
                if visited[nx] != 0:
                    continue
                # [5,10] [5,6] [5,4]
                visited[nx] = visited[x] + 1
                tmp = x_list[:] # 같은 리스트를 참조하지 않도록 하는 방법 -> [:]
                tmp.append(nx)
                q.append(tmp)

BFS()
import random
ran_list = random.choice(result_list)

print(result_val)
print(' '.join(map(str,ran_list)))
'''
예제 입력 1 
5 17
예제 출력 1 
4
5 10 9 18 17
예제 입력 2 
5 17
예제 출력 2 
4
5 4 8 16 17
'''