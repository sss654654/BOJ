import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

X = int(sys.stdin.readline())

li.sort()

breakon = 0
result = 0

### 그리디로 다시 풀어보자

for i in li:
    for j in range(len(li)-1,0,-1):
        if i > li[j]:
            breakon = 1
            break
        if X > i + li[j]:
            break
        elif X < i + li[j]:
            continue
        else:
            result += 1
            break
    if breakon == 1:
            break
    
print(result)