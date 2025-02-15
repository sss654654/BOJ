# <Comparison Sort> : 원소들간의 크기를 비교하여 정렬 수행
# 재귀적으로 수열을 나눠 정렬한 후 합치는 정렬법
# Divide and Conquer algorithm(분할 정복 알고리즘)
# 분할하는 과정의 시간복잡도 O(N)
# 합쳐나가는 과정의 시간복잡도 O(NlogN)
# O(N) < O(NlogN) -> Merge Sort = O(NlogN)

n = [2,6,5,1,7,4,3]
# -> [2,6,5,1] / [7,4,3]
# -> [2,6],[5,1] / [7,4],[3]
# -> [2][6][5][1] / [7][4][3]
# -> [2,6], [1,5] / [4,7] [3]
# -> [1,2,5,6] / [3,4,7]
# -> [1,2,3,4,5,6,7]
def merge_sort(arr):
    if len(arr) > 1: # 리턴되는 배열의 길이가 1보다 크지 않을 경우 더 이상 재귀 x!! 
        left_arr = arr[:len(arr)//2] # [start:mid]
        right_arr = arr[len(arr)//2:] # [mid:end]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0 # 왼쪽 리스트의 인덱스
        j = 0 # 오른쪽 리스트의 인덱스
        k = 0 # 값을 저장할 리스트의 인덱스(i,j에 따라 증가)
        while i < len(left_arr) and j < len(right_arr): # i나 j 둘 중 하나라도 리스트의 길이를 넘을 경우 빠져나가기
            if left_arr[i] < right_arr[j]: # 왼쪽과 오른쪽 리스트의 첫 번째 값을 비교, 더 작은 수를 arr에 대입
                arr[k] = left_arr[i]
                i += 1 # 인덱스가 증가하며 자신의 길이를 넘을 경우 빠져나간 뒤 이후 남은 오른쪽 리스트를 넣을 것
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
            
        # 위에서 오쪽 리스트를 먼저 다 arr에 넣었으면 여기선 왼쪽 리스트를 확인
        while i < len(left_arr): # 위의 반복문에서 j가 빠져나왓을 경우, i 실행
            arr[k] = left_arr[i] # j가 다 입력된 다음의 k 인덱스부터 정렬된 왼쪽 리스트가 대입됨
            k += 1
            i += 1

        # 위에서 왼쪽 리스트를 먼저 다 arr에 넣었으면 여기선 오른쪽 리스트를 확인
        while j < len(right_arr): # 위의 반복문에서 i가 빠져나왓을 경우, j 실행
            arr[k] = right_arr[j] # i가 다 입력된 다음의 k 인덱스부터 정렬된 오른쪽 리스트가 대입됨
            k += 1
            j += 1
        return arr # 왼쪽 리스트, 오른쪽 리스트를 병합한 리스트 반환

import sys
N = int(sys.stdin.readline())
li = []
for i in range(N):
    li.append(int(sys.stdin.readline()))

result = merge_sort(li)

for i in range(N):
    print(result[i])