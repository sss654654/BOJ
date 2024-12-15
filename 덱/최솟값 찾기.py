'''
문제
N개의 수 A1, A2, ..., AN과 L이 주어진다.

Di = A(i-L+1) ~ A(i) 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 
이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

입력
첫째 줄에 N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)

둘째 줄에는 N개의 수 Ai가 주어진다. (-109 ≤ Ai ≤ 109)

출력
첫째 줄에 Di를 공백으로 구분하여 순서대로 출력한다.

예제 입력 1 
12 3
1 5 2 3 6 2 3 7 3 5 2 6
A1 A2 A3 ... A12
D1(1) D2(1 5) D3(1 5 2) D4(5 2 3) D5(2 3 6) D6(3 6 2) 
D7(6 2 3) D8(2 3 7) D9(3 7 3) D10(7 3 5)D11(3 5 2) D12(5 2 6)
예제 출력 1 
1 1 1 2 2 2 2 2 3 3 2 2
'''

# 첫 번째 방법 -> 시간초과
'''
import sys
from collections import deque

N, L = map(int,sys.stdin.readline().split())
find_min = list(map(int, sys.stdin.readline().split()))

result = []
for i in range(1, N+1): # 12 : 0~11
    if i - L < 0: # 1-3, 2-3
        result.append(min(find_min[0:i]))
    else: # 3-3, 4-3
        result.append(min(find_min[i-L:i]))
print(' '.join(map(str,result)))
''' 

# 두 번째 방법
import sys
from collections import deque

N, L = map(int,sys.stdin.readline().split())
find_min = list(map(int, sys.stdin.readline().split()))

min_check = deque()
min_check.append([0, find_min[0]])
result = []
result.append(min_check[-1][1])

for i in range(1, N):
    #print(min_check)
    while min_check and min_check[-1][1] > find_min[i]:
        tmp = min_check.pop()
        #print(f'pop:{tmp}')
    min_check.append([i, find_min[i]])
    if min_check[0][0] <= i-L: # 인덱스(i) 크기가 L부터는 계속해서 범위 값을 벗어날 것임
        min_check.popleft()
    result.append(min_check[0][1])
    # print(result)

print(' '.join(map(str,result)))
'''
    if len_check + len(pop_list) > L:
        if min_check[0][1] < pop_list[0][1]:
            len_check -= 1
            min_check.popleft()
        elif min_check[0][1] > pop_list[0][1]:
            len_check -= 1
            pop_list.popleft()
'''

'''
예제 입력 1 
12 3
1 5 2 3 6 2 3 7 3 5 2 6
D1(1) D2(1 5) D3(1 5 2) D4(5 2 3) D5(2 3 6) D6(3 6 2) 
D7(6 2 3) D8(2 3 7) D9(3 7 3) D10(7 3 5) D11(3 5 2) D12(5 2 6)

예제 출력 1 
1 1 1 2 2 2 2 2 3 3 2 2

5 3
1 3 2 4 4
답: 1 1 1 2 2

12 3
2 5 1 3 6 2 3 7 3 5 2 6
답: 2 2 1 1 1 2 2 2 3 3 2 2
'''