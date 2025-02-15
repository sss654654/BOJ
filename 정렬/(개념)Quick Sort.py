# <Comparison Sort> : 원소들간의 크기를 비교하여 정렬 수행
#  Quicksort
# 1. pivot element 선택 
# 2. 선택한 pivot element보다 작은 element들을 왼쪽 하위 배열에 저장
# 오른쪽 하위 배열에은 pivot element보다 큰 모든 element들을 저장
# 3. 이 두 하위 배열에서 재귀적으로 quickstart를 호출
# 왼쪽 하위 배열에서 quickstart 호출 후 오른쪽 하위 배열에서 quickstart 호출

def quicksort(arr, left, right):
    if left < right:
        part_pos = partition(arr,left,right) # 피봇요소 선택
        # 피봇은 맨 마지막 수를 기준으로 이 수에 대해서 작은 수는 왼쪽에 있고 큰 수는 오른쪽에 있도록 하는 인덱스 위치임
        quicksort(arr,left,part_pos-1) # (part_pos-1) -> 피봇 요소보다 인덱스 작은 모든 요소에 대해 퀵 정렬을 호출
        quicksort(arr,part_pos+1,right) # (part_pos+1) -> 피봇 요소보다 인덱스가 큰 모든 요소에 대해 퀵 정렬을 호출


def partition(arr,left,right):
    # 퀵소트의 첫 단계(피봇 선택) 이후 피벗 요소의 인덱스를 반환
    # [22,11,88,66,55,77,33,44]
    i = left # 22(0)
    j = right-1 # 33(6)
    pivot = arr[right] # 44(7)

    # i가 오른쪽으로 이동하고 j가 왼쪽으로 이동하여 i와 j가 교차할 때까지 이동한다는 것
    while i < j: # i와 j가 교차할 때까지 반복
        while i < right and arr[i] < pivot: # i의 값이 피봇보다 작으면 i를 오른쪽으로 이동
            # 피봇보다 큰 값을 찾기 위해 오른쪽으로 탐색
            i += 1
        while j > left and arr[j] >= pivot: # j의 값이 피봇보다 크거나 같으면 j를 왼쪽으로 이동
            # 피봇보다 작은 값을 찾기 위해 왼쪽으로 탐색
            j -= 1
        if i < j: # 아직 i가 j보다 작을 경우 스왑 진행 후 다시 i,j 증감 진행
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot: # i의 값이 피봇보다 클 경우 i의 값과 피봇 값을 스왑
        arr[i], arr[right] = arr[right], arr[i] # right는 pivot의 위치
    
    return i # 인덱스 i를 반환(왼쪽엔 작은 수의 배열, 오른쪽엔 큰 수의 배열이 있는)


import sys
N = int(sys.stdin.readline())
li = []
for i in range(N):
    li.append(int(sys.stdin.readline()))

quicksort(li,0,len(li)-1)

for i in range(N):
    print(li[i])
    