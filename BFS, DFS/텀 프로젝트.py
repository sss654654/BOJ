'''
문제
이번 가을학기에 '문제 해결' 강의를 신청한 학생들은 텀 프로젝트를 수행해야 한다. 프로젝트 팀원 수에는 제한이 없다. 심지어 모든 학생들이 동일한 팀의 팀원인 경우와 같이 한 팀만 있을 수도 있다. 프로젝트 팀을 구성하기 위해, 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다. (단, 단 한 명만 선택할 수 있다.) 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능하다.

학생들이(s1, s2, ..., sr)이라 할 때, r=1이고 s1이 s1을 선택하는 경우나, s1이 s2를 선택하고, s2가 s3를 선택하고,..., sr-1이 sr을 선택하고, sr이 s1을 선택하는 경우에만 한 팀이 될 수 있다.

예를 들어, 한 반에 7명의 학생이 있다고 하자. 학생들을 1번부터 7번으로 표현할 때, 선택의 결과는 다음과 같다.

1	2	3	4	5	6	7
3	1	3	7	3	4	6
위의 결과를 통해 (3)과 (4, 7, 6)이 팀을 이룰 수 있다. 1, 2, 5는 어느 팀에도 속하지 않는다.

주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다. 
각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)

출력
각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.
'''
import sys
from collections import deque
dx=[0,0]
dy=[1,-1]

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    team = list(map(int, sys.stdin.readline().split()))
    for i in range(len(team)):
        team[i] -= 1
    visited = [0 for i in range(n)]
    def BFS(idx):
        q = deque()
        q.append([[idx],team[idx]])
        while q:
            idx, nx = q.popleft()
            if visited[nx] == 1: # 이미 팀이 이루어져있음
                continue
            if nx not in idx: # idx=[0],nx=1 -> idx[0,1],nx=4 
                idx.append(nx)
                q.append([idx, team[nx]]) 
            else: # 어떻게든 인덱스에 접근하는 친구들끼리는 팀이 이루어짐 -> idx[0,1,4],nx=1
                # (3,6) -> (3,team[6]) -> (3,team[team[6]])
                # (3,6) -> (3,5) -> (3,3)
                ''' # 시간초과
                start = idx.index(nx) # 1
                for i in range(start,len(idx)):
                    visited[idx[i]] = 1
                '''
                # 시간초과
                while True:
                    if nx in idx:
                        visited[idx.pop()] = 1
                    else:
                        break
                return 0
        return -1
    
    for i in range(n):
        if visited[i] == 0:
            BFS(i)
    count = 0
    print(visited.count(0))
'''
7
5
2 5 4 5 2
6
1 3 4 3 2 6
13
2 4 5 2 4 1 8 9 10 11 9 10 10
10
2 5 7 1 6 8 8 3 5 10
10
2 7 10 5 3 3 9 10 6 3
6
2 1 1 2 6 3

// ans
3
2
8
6
8
4

예제 입력 1 
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
예제 출력 1 
3
0

0123456
2026235

// 1) 앞서클 뒷서클
2
5
2 3 1 1 1
5
5 5 4 5 3

// ans
2
2

// 2) 1서클, n서클
2
5
2 3 4 5 1
5
1 2 3 4 5

// ans
0
0

// 3) low 케이스
4
2
1 1
2
2 2
2
1 2
2
2 1

// ans
1
1
0
0
'''