'''
문제
N개의 수가 주어졌을 때, 이를 비내림차순으로 정렬하는 프로그램을 작성하시오.

길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
"""이 수는 절댓값이 1,000,000보다 작거나 같은 정수"""이며, 같은 수가 여러 번 중복될 수도 있다.

출력
첫째 줄부터 N개의 줄에 비내림차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

# <Non-comparison Sort> : 원소들간의 크기를 비교하지 않고 정렬 수행
# 수의 범위가 제한되어 있을 때에는 카운팅 소트를 사용 -> 구현이 간단한 장점!


import sys
N = int(sys.stdin.readline())

# 1
count_val = [[i,0] for i in range(2000001)] # N = 5

for i in range(N):
    a = int(sys.stdin.readline())
    count_val[a+1000000][1] += 1

count_li = [x for x in count_val if x[1]>0]

for i in range(len(count_li)):
    for j in range(count_li[i][1]):
        print(count_li[i][0] - 1000000)

'''
# 2
minus_val = [[i,0] for i in range(1000000)] # -1 ~ -1000000
plus_val = [[i,0] for i in range(1000001)] # 0 ~ 1000000
# 0 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 -1 -2 -3 -4 -5

li = []
for i in range(N):
    a = int(sys.stdin.readline())
    if a < 0: # a=-1,-2,-3...
        minus_val[abs(a)-1][1] += 1 # -1은 인덱스 0 / -2는 인덱스 1
    else:
        plus_val[a][1] += 1

minus_li = [x for x in minus_val if x[1]>0]
plus_li = [x for x in plus_val if x[1]>0]


for i in range(len(minus_li)-1,-1,-1):
    for j in range(minus_li[i][1]):
        print(-(minus_li[i][0]) - 1)
    
for i in range(len(plus_li)):
    for j in range(plus_li[i][1]):
        print(plus_li[i][0])
'''

'''
예제 입력 1 
5
5
4
3
2
1
예제 출력 1 
1
2
3
4
5
예제 입력 2 
5
1
2
1
2
1
예제 출력 2 
1
1
1
2
2
예제 입력 3 
5
1
2
3
4
5
예제 출력 3 
1
2
3
4
5
예제 입력 4 
6
0
0
0
0
0
0
예제 출력 4 
0
0
0
0
0
0
'''