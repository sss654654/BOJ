import sys

card = [i for i in range(1,21)]


for i in range(10):
    a, b = map(int,sys.stdin.readline().split())
    temp = card[a-1:b]
    temp = list(reversed(temp))
    del card[a-1:b]
    for j in temp:
        card.insert(a-1, j)
        a += 1

for i in card:
    print(i, end=" ")