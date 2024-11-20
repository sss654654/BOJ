'''
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
'''

import sys
word = list(sys.stdin.readline().strip())
word2 = list(sys.stdin.readline().strip())

len_words = len(word) + len(word2)
minus = 0
idx = 0
idx2 = 0

while True:
    if word[idx] in word2:
        minus += 2
        word2.remove(word[idx])
    idx += 1
    if idx == len(word):
        break

print(len_words - minus)