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