import sys
N, M = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))
n_list.sort()

arr = [0 for _ in range(N)]

def n_m(k):
    if k == M:
        for i in range(M):
            if i < M -1 and arr[i] > arr[i+1]:
                return
        for i in range(M):
            print(arr[i],end=" ")
        print()
        return
    
    for i in range(len(n_list)):
        arr[k] = n_list[i]
        n_m(k+1)

n_m(0)