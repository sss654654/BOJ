import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
T = int(input())

while T != 0:
    if T < 0:
        break
    T -= 1
    n = int(input())
    selpart = [int(x) for x in input().split()]
    selpart.insert(0, 0)

    totalpair = []

    def recur(me, partner):  # 1,3\
        if me != selpart[partner]:  # 1 != selpart[3]
            if (partner == selpart[partner]):
                totalpair.append(partner)
                return
            recur(me, selpart[partner])
        if me == selpart[partner]:
            totalpair.append(partner)
            return
        return
# [1,3] [2,1] [3,3] [4,7] [5,3] [6,4] [7,6]
    for i in range(1, n+1):
        recur(i, selpart[i])  # [3,7]
    paircount = 0
    for i in range(1, n+1):
        for k in totalpair:
            if i == k:
                paircount += 1
                break
    print(n - paircount)
