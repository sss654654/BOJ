'''
문제
정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)

둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

출력
첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.
'''
import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())

a = deque(map(int, sys.stdin.readline().split()))
b = deque(map(int, sys.stdin.readline().split()))

a_cur = 0
b_cur = 0

result_list = []

while True:
    if not a:
        result_list.append(b.popleft())
        if not b:
            break
        continue
    elif not b:
        result_list.append(a.popleft())
        if not a:
            break
        continue
    if a[0] < b[0]:
        result_list.append(a.popleft())
    else:
        result_list.append(b.popleft())

print(' '.join(map(str,result_list)))
'''
예제 입력 1 
2 2
3 5
2 9
예제 출력 1 
2 3 5 9
예제 입력 2 
2 1
4 7
1
예제 출력 2 
1 4 7
예제 입력 3 
4 3
2 3 5 9
1 4 7
예제 출력 3 
1 2 3 4 5 7 9
'''