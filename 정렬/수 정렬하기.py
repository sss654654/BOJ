'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
import sys
N = int(sys.stdin.readline())
li = []
for i in range(N):
    li.append(int(sys.stdin.readline()))

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2] # arr[0] ~ arr[mid]
        right_arr= arr[len(arr)//2:] # arr[mid] ~ arr[-1]

        # 배열 나누기
        merge_sort(left_arr)
        merge_sort(right_arr)

        # 병합
        l_idx = 0
        r_idx = 0
        k = 0
        while l_idx < len(left_arr) and r_idx < len(right_arr):
            # 왼, 오 둘 중 하나라도(or) 다 탐색했으면 탈출
            if left_arr[l_idx] < right_arr[r_idx]:
                # 왼쪽, 오른쪽 리스트의 첫번째 값을 비교해서 더 작은 값을 배열에 넣기
                arr[k] = left_arr[l_idx]
                k += 1
                l_idx += 1
            elif left_arr[l_idx] > right_arr[r_idx]:
                arr[k] = right_arr[r_idx]
                k += 1
                r_idx += 1

        while l_idx < len(left_arr): # 아직 왼쪽 리스트에 탐색하지 않은 수가 남아있다면
            arr[k] = left_arr[l_idx]
            k += 1
            l_idx += 1
            
        while r_idx < len(right_arr): # 아직 왼쪽 리스트에 탐색하지 않은 수가 남아있다면
            arr[k] = right_arr[r_idx]
            k += 1
            r_idx += 1
        return arr
    else:
        return arr

result = merge_sort(li)


for i in range(N):
    print(result[i])

'''
li.sort()
for i in range(N):
    print(li[i])

'''

'''
예제 입력 1 
5
5
2
3
4
1
예제 출력 1 
1
2
3
4
5
'''