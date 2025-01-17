'''
문제
N개의 정수로 이루어진 수열이 있을 때, 
크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. 
(1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 
주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
'''
import sys
N, S = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))
result = 0

arr = [0 for i in range(N)]
is_used = [0 for i in range(N)]
count = 0

def back(k):
    global count
    for i in range(1, N+1):
        if k == i:
            for j in range(i):
                if j < i - 1 and arr[j] > arr[j+1]:
                    return
            sum = 0
            for j in range(i):
                sum += arr[j]
            if sum == S:
                print(k, arr,sum)
                count += 1
                return
    for i in range(len(n_list)):
        if not is_used[i]:
            arr[k] = n_list[i]
            is_used[i] = 1
            back(k+1)
            is_used[i] = 0
back(0)
print(count)

'''
예제 입력 1 
5 0
0 0 0 0 0
5 0
-7 -3 -2 5 8
예제 출력 1 
1

'''