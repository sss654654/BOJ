import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

check = [0 for i in range(n)]


X = int(sys.stdin.readline())
li.sort()
# print(li)
# [1, 2, 3, 5, 7, 9, 10, 11, 12]

result = 0
st = 0
end = len(li) - 1

while st < end:
     tmp = li[st] + li[end]

     if tmp == X:
          result += 1
     if tmp < X:
          st += 1
          continue
     end -= 1

# 2, 3, 5, 6, 10
print(result)