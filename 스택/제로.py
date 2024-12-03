import sys

K = int(sys.stdin.readline().strip())

integers = []

for i in range(K):
    integer = int(sys.stdin.readline().strip())
    if integer == 0:
        integers.pop()
        continue
    integers.append(integer)

print(sum(integers))