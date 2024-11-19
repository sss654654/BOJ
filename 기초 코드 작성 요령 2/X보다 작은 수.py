import sys

# N = int(sys.stdin.readline())
N, X = map(int,sys.stdin.readline().split())
N_list = list(map(int,sys.stdin.readline().split())) 

value_list = []

for idx in range(N):
    if N_list[idx] < X:
        value_list.append(N_list[idx])

for idx in range(len(value_list)):
    print('{0}'.format(value_list[idx]), end=' ')
    # print('{}'.format(value_list[idx]), end=' ')
    # print(f'{value_list[idx]}')