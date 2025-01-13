import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# n = 8-> 8x8
# paper(n)
# paper(n//2)
result = []
def recur(x,y,n):
    color = paper[x][y]
    for i in range(x, x+n): # 자신의 위치에서 자신이 속한 사각형의 범위 끝부분까지
        for j in range(y, y+n):
            if color != paper[i][j]:
                recur(x,y,n//2) # 1
                recur(x,y+n//2,n//2) # 2
                recur(x+n//2,y,n//2) # 3
                recur(x+n//2,y+n//2,n//2) # 4
                return
    result.append(color) # 분리되지 않고 확정된 색종이의 색깔을 집어넣음

recur(0,0,N)
print(result.count(0))
print(result.count(1))

'''
result = []
def recur(x,y,n):
    color = paper[x][y]
    # 각 사분면의 첫 번째만 비교
    # n=8 -> 0,0 / 0,4 / 4,0 / 4,4
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j]: # 현재 색깔과 다른 색깔들은 각각의 사분면에서 사등분되어 다시 색깔 체크 
                recur(x, y, n//2) # 1
                recur(x, y+n//2, n//2) # 2
                recur(x+n//2, y, n//2) # 3
                recur(x+n//2, y+n//2, n//2) # 4
                return
    if color == 1:
        result.append(color)
    else:
        result.append(color)

recur(0,0,N)

print(result.count(0))
print(result.count(1))

'''

'''
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
'''