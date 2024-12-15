'''
문제
선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 
이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 
배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

함수는 조합해서 한 번에 사용할 수 있다. 
예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 
예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.

배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ xi ≤ 100)

전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

출력
각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.
'''

import sys
import re
from collections import deque
T = int(sys.stdin.readline())


for i in range(T):
    is_error = 0
    # RDD -> 4 -> [1,2,3,34]
    p = list(sys.stdin.readline().strip()) # 'RDD'
    n = int(sys.stdin.readline()) # 4
    x = sys.stdin.readline().strip() # '[1,2,3,34]'
    
    # 대괄호 내부 내용만 추출
    tmp = re.compile('\[([^]]+)\]') 
    x = tmp.findall(x) # ['1,2,3,34']
    if len(x) != 0: # x의 길이가 0이면 요소가 안담긴채로 입력된 것 -> []
        # x의 길이가 0이 아니면 요소가 담긴 것이므로 split()을 사용해 반점을 기준으로 문자열을 리스트로 변환
        x = x[0]
        x = re.split(',', x)
        # x = deque([int(num) for num in x if num.isdigit()])
    nums = deque(x) 
    try_r = 0 # 짝수면 문자열 그대로 홀수면 뒤집힌 문자열
    for pdx in range(len(p)):
        if p[pdx] == 'R':
            try_r += 1 # 뒤집힌 횟수 덧셈
        elif p[pdx] == 'D':
            if nums: 
                if try_r % 2 != 0: # 짝수(문자열 안바뀜)
                    nums.pop() # 우측 숫자 빼기
                else: # 홀수(문자열 반전되어있음)
                    nums.popleft() # 좌측 숫자 빼기
            else: # 요소를 제거해야하는데 배열이 비어있는 경우
                is_error = 1
    if is_error == 1:
        print('error')
    else:
        if try_r % 2 != 0: # 뒤집힌 횟수가 홀수면 배열 뒤집기
            nums.reverse()
        print('[',end='')
        for idx in range(len(nums)):
            if idx != len(nums) - 1:
                print(nums[idx], end=',')
            else:
                print(nums[idx], end='')
        print(']')


'''
예제 입력 1 
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
예제 출력 1 
[2,1]
error
[1,2,3,5,8]
error
'''
'''
1
R
0
[]

answer
[]

1
D
0
[]

answer
error

1
DDDD
0
[]

answer
error

1
R
1
[123]

answer
[123]


1
D
1
[22]

answer
[]


1
RD
0
[]

answer
error


1
DR
1
[22]

answer
[]


1
DRDR
1
[1]

answer
error


1
D
2
[1,2]

answer
[2]


2
R
3
[1,2,3]
R
0
[]

answer
[3,2,1]
[]


1
DRDDRD
8
[8,7,6,5,4,3,2,1]

answer 
[6,5,4,3]


1
RDRDRD
7
[2,4,6,8,10,12,14]

answer 
[10,8,6,4]
'''