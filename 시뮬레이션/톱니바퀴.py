'''
서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전
입력
첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태가 주어진다. 
상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.

다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다. 
각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 
방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

출력
총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다. 점수란 다음과 같이 계산한다.

1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
'''


# 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전 / dir은 방향(1:시계, -1:반시계)

def rotate(w_list, dir):
    if dir == 1:
        tmp = w_list.pop()
        w_list.appendleft(tmp)
    elif dir == -1:
        tmp = w_list.popleft()
        w_list.append(tmp)
    return w_list

import sys 
from collections import deque
wheel_list = [deque(map(int,sys.stdin.readline().strip())) for _ in range(4)]
K = int(sys.stdin.readline())
# (0->1->2->3->4->5->6->7)
# 왼쪽 톱니바퀴의 인덱스 2과 오른쪽 톱니바퀴의 인덱스 6이 맞닿아 있음
rotate_stack = []
for k in range(1,K+1):
    num, dir  = map(int,sys.stdin.readline().split()) # num은 바퀴 번호, dir은 방향(1:시계, -1:반시계)
    rotate_stack.append([num,dir,1,0])
    while rotate_stack:
        tmp_num, tmp_dir, is_first, left_or_right = rotate_stack.pop()
        idx = tmp_num - 1
        if tmp_num == 1: # 첫번째 톱니바퀴
            if is_first == 1: # 선택에 의한 회전
                if wheel_list[idx][2] != wheel_list[idx+1][6]: # 그리고나서 마주하고있는 톱니바퀴(2) 부분의 극이 다르면
                    rotate_stack.append([tmp_num+1,tmp_dir*-1,0,1])
                    # 세번째 인덱스 0은 첫 선택이 아닌 전파에 의한 회전을 의미
                    # 네번째 인덱스 1은 우측으로 향하는 전파임을 의미
                wheel_list[idx] = rotate(wheel_list[idx], tmp_dir) # 일단 선택한 톱니바퀴가 현재 방향(dir)대로 돌아감
            elif is_first == 0: # 전파에 의한 회전 -> 1이 마지막이므로 더 이상 스택에 안넣어도 됨
                wheel_list[idx] = rotate(wheel_list[idx], tmp_dir)

        elif tmp_num == 2 or tmp_num == 3: # 두번째 톱니바퀴, 세번째 톱니바퀴
            if is_first == 1: # 처음 톱니바퀴 선택에 의한 회전(양옆)
                if wheel_list[idx][2] != wheel_list[idx+1][6]: # 마주하고있는 우측 톱니바퀴 부분의 극이 다르면
                    rotate_stack.append([tmp_num+1,tmp_dir*-1,0,1]) 
                    # 우측(left_or_right:1)으로 회전 전파(is_first:0)
                if wheel_list[idx][6] != wheel_list[idx-1][2]: # 마주하고있는 좌측 톱니바퀴 부분의 극이 다르면
                    rotate_stack.append([tmp_num-1,tmp_dir*-1,0,0]) 
                    # 좌측(left_or_right:0)으로 회전 전파(is_first:0)
                wheel_list[idx] = rotate(wheel_list[idx], tmp_dir) # 현재 방향(dir)대로 돌아감
                    
            elif is_first == 0: # 전파에 의한 회전(좌or우)
                # 1은 전파가 왔으면 돌기만 하면 되지만, 2는 1에서 왔냐 3에서 왔냐에 따라서 또 전파를 해야함
                if left_or_right == 1: # 우측 전파
                    if wheel_list[idx][2] != wheel_list[idx+1][6]: # 마주하고있는 우측 톱니바퀴 부분의 극이 다르면
                        rotate_stack.append([tmp_num+1,tmp_dir*-1,0,1]) # 계속 우측(1)으로 회전 전파(0)
                elif left_or_right == 0: # 좌측 전파
                    if wheel_list[idx][6] != wheel_list[idx-1][2]: # 마주하고있는 좌측 톱니바퀴 부분의 극이 다르면
                        rotate_stack.append([tmp_num-1,tmp_dir*-1,0,0]) # 좌측(0)으로 회전 전파(0)
                wheel_list[idx] = rotate(wheel_list[idx], tmp_dir) # 현재 방향(dir)대로 돌아감

        elif tmp_num == 4: # 네번째 톱니바퀴
            if is_first == 1: # 선택에 의한 회전
                if wheel_list[idx][6] != wheel_list[idx-1][2]: # 그리고나서 마주하고있는 톱니바퀴(3) 부분의 극이 다르면
                    rotate_stack.append([tmp_num-1,tmp_dir*-1,0,0])
                    # 세번째 인덱스 0은 첫 선택이 아닌 전파에 의한 회전을 의미
                    # 네번째 인덱스 0은 좌측으로 향하는 전파임을 의미
                wheel_list[idx] = rotate(wheel_list[idx], tmp_dir) # 일단 선택한 톱니바퀴가 현재 방향(dir)대로 돌아감
            elif is_first == 0: # 전파에 의한 회전 -> 4가 마지막이므로 더 이상 스택에 안넣어도 됨
                wheel_list[idx] = rotate(wheel_list[idx], tmp_dir)

result = 0
for i in range(4):
    if i == 0:
        if wheel_list[i][0] == 1:
            result += 1
    elif i == 1:
        if wheel_list[i][0] == 1:
            result += 2
    elif i == 2:
        if wheel_list[i][0] == 1:
            result += 4
    elif i == 3:
        if wheel_list[i][0] == 1:
            result += 8

print(result)


'''
00000000
00000000
00000000
00000000
0
예제 입력 1 
10101111
01111101
11001110
00000010
2
3 -1
1 1
예제 출력 1 
7
예제 입력 2 
11111111
11111111
11111111
11111111
3
1 1
2 1
3 1
예제 출력 2 
15

예제 입력 3 
10001011
10000011
01011011
00111101
5
1 1
2 1
3 1
4 1
1 -1
예제 출력 3 
6

예제 입력 4 
10010011
01010011
11100011
01010101
8
1 1
2 1
3 1
4 1
1 -1
2 -1
3 -1
4 -1
예제 출력 4 
5
'''