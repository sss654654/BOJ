'''
문제
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. 
(이 위치는 가장 처음 큐에서의 위치이다.) 
이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.


입력
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. 
N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 
둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 
위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.
'''
import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
r_queue = deque(i for i in range(1, N + 1))
select_idx = list(map(int,sys.stdin.readline().split()))
#print(r_queue)
#print(select_idx)

check_point = int(len(r_queue) / 2)
# 8, 9 -> 4
# 10, 11 -> 5
# 12, 13 -> 6
result = 0
for i in range(M):
    check_idx = r_queue.index(select_idx[i]) 
    # 2 9 5 각각의 인덱스가 check_idx에 담김
    # ex) 2는 r_queue에서 인덱스 1에 있음
    while True:
        if select_idx[i] == r_queue[0]:
            if r_queue:
                r_queue.popleft()
            check_point = int(len(r_queue) / 2)
            break
        else:
            # 체크포인트는 항상 중앙 값, 체크포인트에 체크 인덱스를 뺀 값의 절댓값 크기에 따라 이동방향 설정
            if check_point >= check_idx: # 인덱스가 체크포인트 좌측에 있으므로, 좌측이동
                r_queue.append(r_queue.popleft())
                result += 1
            elif check_point < check_idx: # 인덱스가 체크포인트 우측에 있으므로, 우측이동
                r_queue.appendleft(r_queue.pop())
                result += 1
print(result)
'''
1 2 3 4 5 (6) 7 8 9 10 11 -> 홀수 : 좌측이동이 더 짧음 why? 중심점이 왼쪽에 치우쳐있기 때문
1 2 3 4 5 (6) 7 8 9 10 -> 짝수 : 좌/우측 이동의 거리가 다르지 않음

예제 입력 2 
10 3
2 9 5
1 2 3 4 5 (6) 7 8 9 10
2 3 4 5 6 (7) 8 9 10 1(<-)(o)

1 2 3 4 5 6 7 8 9 10(->)
10 1 2 3 4 5 6 7 8 9(->)
9 10 1 2 3 4 5 6 7 8(->)(o)

8 9 10 1 2 3 4 5 6 7(->)
7 8 9 10 1 2 3 4 5 6(->)
6 7 8 9 10 1 2 3 4 5(->)
5 6 7 8 9 10 1 2 3 4(->)

예제 출력 2 
8

예제 입력 1 
10 3
1 2 3
예제 출력 1 
0

예제 입력 3 
32 6
27 16 30 11 6 23
예제 출력 3 
59

예제 입력 4 
10 10
1 6 3 2 7 9 8 4 10 5
예제 출력 4 
14
'''