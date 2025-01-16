'''
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''
import sys
N,M = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))
n_list.sort()
arr = [0 for _ in range(len(n_list))]
is_used = [0 for _ in range(len(n_list))]

result = []
def n_m(k):
    if k == M:
        tmp = ""
        for i in range(M):
            tmp += str(arr[i])
            if i != M -1:
             tmp += " "
        result.append(tmp)
        return
    for i in range(len(n_list)):
        if not is_used[i]:
            arr[k] = n_list[i]
            is_used[i] = 1
            n_m(k+1)
            is_used[i] = 0

n_m(0)
result = list(set(result))
result_real = []
for i in range(len(result)):
    result_real.append(list(map(int,result[i].split())))
result_real.sort()

for i in range(len(result)):
    for j in range(M):
        print(result_real[i][j], end=" ")
    print()
    
    
'''
input:
3 2
1 12 21
   
output:
1 12 
1 21
12 1
12 21
21 1
21 12
예제 입력 1 
3 1
4 4 2
예제 출력 1 
2
4
예제 입력 2 
4 2
9 7 9 1
예제 출력 2 
1 7
1 9
7 1
7 9
9 1
9 7
9 9
예제 입력 3 
4 4
1 1 1 1
예제 출력 3 
1 1 1 1
'''