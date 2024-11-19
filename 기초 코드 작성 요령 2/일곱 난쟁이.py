"""
import sys

dwarf = []
dsum = 0


for i in range(9):
    h = int(sys.stdin.readline())
    dwarf.append(h)
    dsum += h
    
dh = len(dwarf)
notd1 = 0
notd2 = 0 
for i in range(dh-1):
    for j in range(i+1, dh):
        if dsum - (dwarf[i] + dwarf[j]) == 100:
            notd1 = dwarf[i]
            notd2 = dwarf[j]
            break
    if len(dwarf) != dh:
        break


        
dwarf.sort()

dwarf.remove(notd1)
dwarf.remove(notd2)

for i in dwarf:
    print(i)
"""

import sys

dwarfs = []

for i in range(9):
    dwarf = int(sys.stdin.readline())
    dwarfs.append(dwarf)

dwarfs.sort()

sum_dwarfs = sum(dwarfs)
len_dwarfs = len(dwarfs)
select_dwarfs = sum_dwarfs - 100

idx1 = 0
idx2 = 0

while True:
    for j in range(idx1 + 1, len_dwarfs):
        if dwarfs[idx1] + dwarfs[j] == select_dwarfs:
            idx2 = j
            break
    if dwarfs[idx1] + dwarfs[idx2] == select_dwarfs:
        dwarfs.remove(dwarfs[idx1])
        dwarfs.remove(dwarfs[idx2-1])
        break
    idx1 += 1


for idx in range(len(dwarfs)):
    print(f'{dwarfs[idx]}')

