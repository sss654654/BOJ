'''
가장 잘 알려진 풀이는 스택을 두 개 사용하는 것이다.

커서를 기준으로 왼쪽에 위치한 스택과 오른쪽에 위치한 스택 두 개를 만든다.

오른쪽 스택은 방향을 뒤집어두었다. pop 하면 왼쪽에 있는 원소가 나오고, append도 왼쪽에 된다.

처음에는 문장의 맨 뒤에 커서가 위치하므로 왼쪽 스택에 문자를 순서대로 넣어두면 된다. 커서는 항상 left 리스트 오른쪽에 있다.
'''

import sys

N = list(sys.stdin.readline().strip())
N_tmp = []
M = int(sys.stdin.readline())
cur = len(N)

for i in range(M):
    com = list(map(str,sys.stdin.readline().split()))
    if com[0] == "P":
        N.append(com[1])
        cur += 1
    elif com[0] == "L":
        if cur != 0:
            N_tmp.append(N.pop())
            cur -= 1
    elif com[0] == "D":
        if N_tmp:
            N.append(N_tmp.pop())
            cur += 1
    elif com[0] == "B":
        if cur != 0:
            N.pop()
            cur -= 1
N_tmp.reverse()
print(''.join(N) + ''.join(N_tmp))

'''
[ a b c d ]
[0,1,2,3,4]
'''