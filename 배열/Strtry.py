'''
import sys

N = int(sys.stdin.readline())

lalpa = [0 for i in range(26)]
ralpa = [0 for i in range(26)]

for i in range(N):
    l, r = map(str,sys.stdin.readline().split())

    for li in l:
        lalpa[ord(li) - ord('a')] += 1

    for ri in r:
        ralpa[ord(ri) - ord('a')] += 1

    if lalpa != ralpa:
        print("Impossible")
    else:
        print("Possible")

    lalpa = [0 for i in range(26)]
  possible = 1
possible_list = []  ralpa = [0 for i in range(26)]

'''

import sys

N = int(sys.stdin.readline())
is_possible = 1
for i in range(N):
    is_possible = 1
    a, b = map(list, sys.stdin.readline().split())
    if len(a) != len(b):
        print("Impossible")
        is_possible = 0
        continue
    for aidx in range(len(a)):
        if a[aidx] not in b:
            print("Impossible")
            is_possible = 0
            break
        else:
            b.remove(a[aidx])
    if is_possible == 0:
        continue
    print("Possible")