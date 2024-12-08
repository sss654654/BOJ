import sys

N = int(sys.stdin.readline())


list = []
for i in range(N):
    h = int(sys.stdin.readline())
    list.append(h)

stack = [] # [[볼 수 있는 빌딩의 수, 빌딩 높이],[...],...]
result = 0

for i in range(len(list)):
    while stack:
        # 스택의 맨 위와 빌딩을 순서대로 비교
        if stack[-1][1] > list[i]: # 스택의 맨 위 빌딩이 더 높으면 반복문 탈출
                    break
        else: # 스택의 맨 위 빌딩이 더 낮으면 스택에서 뺀 후, 볼 수 있는 빌딩의 수를 결과에 더함.
            tmp = stack.pop()
            result += tmp[0]
            if stack:
            # 스택이 남아있으면 팝된 스택의 볼 수 있는 빌딩의 수를 남아있는 스택의 탑의 볼 수 있는 빌딩의 수에 더함
                stack[-1][0] += tmp[0] + 1 
    stack.append([0, list[i]]) # 스택에 빌딩을 순서대로 푸쉬

# 현재 스택에는 빌딩들이 각각 자신이 볼 수 있는 빌딩의 수를 가진채로 존재함
# 또한 스택의 탑(마지막 빌딩)은 푸쉬 후 반복문을 바로 빠져나오며 비교가 안된 상태 

tmp = stack.pop()
if stack: # 스택의 탑(마지막 빌딩)을 팝한 후 스택이 남아있으면,
   if stack[-1][1] > tmp[1]: # 또한 남아있는 스택의 탑의 빌딩이 팝한 빌딩보다 높으면 남아있는 빌딩에 +1
        stack[-1][0] += 1 

while stack: # 현재 스택에는 전부 계산된(볼 수 있는 빌딩) 빌딩만이 존재 
    # 즉, 위와 똑같은 방식으로 팝 할 때마다 스택의 탑에 더함
        tmp = stack.pop()
        result += tmp[0]
        if stack:
            stack[-1][0] += tmp[0] + 1 

print(result)

'''
6
10
3
7
4
12
2

input:
10
5
1
4
1
3
1
2
1
1
1
output:21
answer:24(9 + 0 + 7 + 0 + 5 + 0 + 3 + 0 + 0 + 0)
'''