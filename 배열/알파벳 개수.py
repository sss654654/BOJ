import sys


S = sys.stdin.readline().strip()

alpa = [0 for i in range(26)]
for i in S:
    alpanum = ord(i) - ord('a')
    alpa[alpanum]+= 1

for i in range(26):
    if i != 25:
        print(alpa[i], end=" ")
    else:
        print(alpa[i])
