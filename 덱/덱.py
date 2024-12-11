'''
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque()
result_queue = deque()
for i in range(N):
    queue.append(list(map(str,sys.stdin.readline().split())))
    if queue[i][0] == 'push_front':
        result_queue.appendleft(queue[i][1])
    elif queue[i][0] == 'push_back':
        result_queue.append(queue[i][1])
    elif queue[i][0] == 'pop_front':
        if result_queue:
            print(result_queue.popleft())
        else:
            print(-1)
    elif queue[i][0] == 'pop_back':
        if result_queue:
            print(result_queue.pop())
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
