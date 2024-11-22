'''
import sys

N = sys.stdin.readline().strip()

set = [0 for i in range(10)]

for i in N:
    set[int(i)] += 1

max = 0
sixnine = 0

for i in range(len(set)):
    if i == 6 or i == 9:
        sixnine += set[i]
    else:
        if max < set[i]:
            max = set[i]
            
quo = int(sixnine / 2)
rem = sixnine % 2

if max < quo + rem:
    max = quo + rem

print(max)
'''

import sys

N = list(sys.stdin.readline().strip())

num_sets = [0 for i in range(10)]

for ni in range(len(N)):
    num_sets[int(N[ni])] += 1

sn = num_sets[6] + num_sets[9]
if sn > 1:
    num_sets[6] = int(sn / 2) + (sn % 2)
    num_sets[9] = 0

print(max(num_sets))
