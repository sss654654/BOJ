from collections import deque
import sys

n = int(sys.stdin.readline())

sequence = deque() # 수열을 담을 수열스택

for i in range(n):
    num = int(sys.stdin.readline())
    sequence.append(num)

num = 0 # 1부터 n까지의 수를 수열로 만들기 위한 첫번째 수
idx = 0 # 스택과 수열을 비교하기 위해 수열을 탐색하는 인덱스
is_result = 1 # 답을 낼 수 있으면 1, 답을 낼 수 없으면(NO) 0

stack = deque() # 수열을 만들기 위해 push, pop을 수행하는 스택
print_result = deque() # +, -가 담기는 결과출력 스택
result = deque() # stack에서 pop한 수를 넣는택 결과 스택 

while True:
    if stack:
        if stack[len(stack) - 1] != sequence[idx]:
            num += 1
            stack.append(num)
            print_result.append('+')
        else:
            result.append(stack.pop())
            print_result.append('-')
            idx += 1
    else:
        num += 1
        stack.append(num)
        print_result.append('+')

    if result == sequence: # 결과 스택과 초기 스택이 같으면 탈출
        break
    if num > n: # 스택에 넣을 숫자가 초기 설정한 n을 초과하면 is_result를 0으로 만들고 탈출
        is_result = 0
        break
   
if is_result:
    for i in range(len(print_result)):
        print(print_result[i])
else:
    print("NO")

'''
[stack] [result]   
[1 2 3 4] [] ++++
[1 2 3] [4] -
[1 2] [4 3] -
[1 2 5] [4 3] +
[1 2 5 6] [4 3] +
[1 2 5] [4 3 6] -
[1 2 5 7] [4 3 6] +
[1 2 5 7 8] [4 3 6] +
[1 2 5 7] [4 3 6 8] -
[1 2 5] [4 3 6 8 7] -
[1 2] [4 3 6 8 7 5] -
[1] [4 3 6 8 7 5 2] -
[] [4 3 6 8 7 5 2 1] -
'''
# sequence -> [4 3 6 8 7 5 2 1]

'''
[stack] [result]   
[1] []
[] [1]
[2] [1]
[] [1 2]
[3] [1 2]
[3 4] [1 2]
[3 4 5] [1 2]
[3 4] [1 2 5]
[3] [1 2 5 4] !!!
'''
# sequence -> [1 2 5 3 4]
