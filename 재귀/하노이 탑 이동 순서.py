'''
n-1개의 원판을 기둥 1에서 기둥2로 옮긴다.
n번 원판을 기둥1에서 기둥3으로 옮긴다.
n-1개의 원판을 기둥 2에서 기둥 3으로 옮긴다.
-> 원판이 n-1개일 때 옮길 수 있으면 원판이 n개일 때에도 옮길 수 있다.

원판이 1개일 때 원판을 내가 원하는 곳으로 옮길 수 있다.
원판이 k개일 때 옮길 수 있으면 원판이 k+1일 때에도 옮길 수 있다.
'''
# a기둥(1), b기둥(2), 6-a-b기둥(3,1+2+3=6)
# n-1개의 원판을 기둥 a에서 기둥 6-a-b로 옮긴다. -> hanoi(a,6-a-b,n-1)
# n번 원판을 기둥 a에서 기둥 b로 옮긴다. -> result.append(f'{a} {b}')
# n-1개의 원판을 기둥 6-a-b에서 기둥 b로 옮긴다. -> hanoi(6-a-b,b,n-1)
def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
    hanoi_tower(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계
    
import sys
N = int(sys.stdin.readline())
print(2**N-1)
hanoi_tower(N, 1, 3)