"""
import sys

N = int(sys.stdin.readline())

use = list(map(int,sys.stdin.readline().split()))

Y = 0
M = 0

for i in use:
    Yval = int(i / 30) + 1
    Y += Yval*10

    Mval = int(i / 60) + 1
    M += Mval*15

if Y == M:
    print("Y M {}".format(Y))
elif Y > M:
    print("M {}".format(M))
elif Y < M:
    print("Y {}".format(Y))
"""

import sys

N = int(sys.stdin.readline())

use = list(map(int,sys.stdin.readline().split()))

y_quot = 0
y_sum = 0
m_quot = 0
m_sum = 0

for idx in range(len(use)):
    m_quot = int(use[idx] / 60)
    if m_quot > 0:
        m_sum += (m_quot + 1) * 15
    else:
        m_sum += 15

    y_quot = int(use[idx] / 30)
    if y_quot > 0:
        y_sum += (y_quot + 1) * 10
    else:
        y_sum += 10

if y_sum < m_sum:
    print(f"Y {y_sum}")
elif y_sum > m_sum:
    print(f"M {m_sum}")
else:
    print(f"Y M {m_sum}")