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
    ralpa = [0 for i in range(26)]