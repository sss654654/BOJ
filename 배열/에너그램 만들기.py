import sys


falpa = [0 for i in range(26)]
salpa = [0 for i in range(26)]


first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

for fi in first:
    falpa[ord(fi) - ord('a')] += 1

for si in second:
    salpa[ord(si) - ord('a')] += 1

ans = 0


for i in range(26):
    if falpa[i] > salpa[i]:
        ans += falpa[i] - salpa[i]
    elif falpa[i] < salpa[i]:
        ans += salpa[i] - falpa[i]
        
print(ans)