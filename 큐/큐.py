'''
문제
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
'''
import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque()
result_queue = deque()
for i in range(N):
    queue.append(list(map(str,sys.stdin.readline().split())))
    if queue[i][0] == 'push':
        result_queue.append(queue[i][1])
    elif queue[i][0] == 'pop':
        if result_queue:
            print(result_queue.popleft())
        else:
            print(-1)
    elif queue[i][0] == 'size':
        print(len(result_queue))
    elif queue[i][0] == 'empty':
        if result_queue:
            print(0)
        else:
            print(1)
    elif queue[i][0] == 'front':
        if result_queue:
            print(result_queue[0])
        else:
            print(-1)
    elif queue[i][0] == 'back':
        if result_queue:
            print(result_queue[-1])
        else:
            print(-1)


'''
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

1
2
2
0
1
2
-1
0
1
-1
0
3
'''