'''
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
'''

import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split())) 
x = int(sys.stdin.readline())

n_list.sort()

st = 0
end = len(n_list) - 1
answer = 0

while st < end:
     tmp = n_list[st] + n_list[end]
     if tmp == x:
          answer += 1
     if tmp < x:
          st += 1
          continue
     end -= 1
        
print(answer)

'''
9
5 12 7 10 9 1 2 3 11
13
5 12 7 10 9 1 2 3 11
'''