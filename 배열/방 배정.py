import sys

N, K = map(int,sys.stdin.readline().split())

m_grade = [0 for i in range(6)]
w_grade = [0 for i in range(6)]

for i in range(N):
    S, Y = map(int,sys.stdin.readline().split())
    if S == 0: # Woman
        w_grade[Y - 1] += 1
    elif S == 1: # Man
        m_grade[Y - 1] += 1

wm_sum = 0

for m in range(len(m_grade)):
    wm_sum += int(m_grade[m] / K)
    if m_grade[m] % K != 0:
        wm_sum += 1
    wm_sum += int(w_grade[m] / K)
    if w_grade[m] % K != 0:
        wm_sum += 1
    # M : 15 , K = 4
print(wm_sum)