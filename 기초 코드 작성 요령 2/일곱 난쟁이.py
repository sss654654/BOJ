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

    