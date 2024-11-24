import sys

N = int(sys.stdin.readline().rstrip())

key_log = []
for i in range(N):
    key_log = list(map(str, sys.stdin.readline().rstrip()))
    cur = 0
    left_kl = []
    right_kl = []
    for j in range(len(key_log)):
        if key_log[j].isalpha() | key_log[j].isalnum():
            cur += 1
            left_kl.append(key_log[j])
        elif key_log[j] == '>':
            if right_kl:
                left_kl.append(right_kl.pop())
                cur += 1
        elif key_log[j] == '<':
            if left_kl:
                right_kl.append(left_kl.pop())
                cur -= 1
        elif key_log[j] == '-':
            if left_kl:
                left_kl.pop()
                cur -= 1
    right_kl.reverse()
    print(''.join(left_kl) + ''.join(right_kl))