import sys

N = int(sys.stdin.readline())
my_stack = []

for i in range(N):
    com = list(map(str,sys.stdin.readline().split())) # push 1 -> [push, 1]
    if com[0] == 'push':
        my_stack.append(com[1])
    elif com[0] == 'pop':
        if not my_stack:
            print(-1)
            continue
        print(my_stack.pop())
    elif com[0] == 'size':
        print(len(my_stack))
    elif com[0] == 'empty':
        if not my_stack:
            print(1)
            continue
        print(0)
    elif com[0] == 'top':
        if not my_stack:
            print(-1)
            continue
        print(my_stack[len(my_stack) - 1])