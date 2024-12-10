'''
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. 
Ai의 오큰수는 '오른쪽에 있으면서' Ai보다 큰 수 중에서 '가장 왼쪽에 있는 수'를 의미한다. 
그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. 
A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.
'''
import sys

N = int(sys.stdin.readline())

seq_a = list(map(int,sys.stdin.readline().split()))

stack = []
result = [-1 for i in range(N)]

for i in range(N):
    while stack:
        if stack[-1][0] < seq_a[i]: # 스택의 탑보다 현재 리스트 값이 크다면
            result[stack[-1][1]] = seq_a[i] 
            # 스택 탑의 인덱스를(stack[-1][1]) 결과 리스트의 인덱스로 사용해 -1 대신 현재 리스트 값 넣기
            stack.pop()
        else:
            break
    stack.append([seq_a[i], i]) # [값, 인덱스]

print(' '.join(map(str, result)))

# split()은 양 옆의 공백을 없애는 함수

'''
예제 입력 1 
4
3 5 2 7
예제 출력 1 
5 7 7 -1

예제 입력 2 
4
9 5 4 8
예제 출력 2 
-1 8 8 -1
'''