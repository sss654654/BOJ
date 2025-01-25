'''
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''
import sys
N = int(sys.stdin.readline())
is_used = [0 for _ in range(N)]
result = 0
def is_queen(x):
    for i in range(x): # i, is_used[i] -> x,y
        # 방금 놓은 퀸의 위치-> [x,is_used[x]]
        # 지금까지 놓은 퀸의 위치 -> [i,is_used[i]]
        if is_used[x] == is_used[i] or abs(is_used[x] - is_used[i]) == abs(x-i): 
            # (0,1),(2,1) -> y가 겹치면 안됨
            # (3,0),(1,2) -> 우상향 곡선이면 안됨
            # (1,1),(3,3) -> 좌상향 곡선이면 안됨
            return False
    return True


def queen(x):
    global result
    if x == N:
        result += 1
        return
    else:
        for i in range(N):
            is_used[x] = i # is_used[x][i] 에 퀸을 놓는다
            if is_queen(x): # 퀸의 경로에 걸리지 않으면 다음 라인(x)으로 넘어간다
                queen(x+1)
queen(0)
print(result)

'''
예제 입력 1 
8
예제 출력 1 
92
'''