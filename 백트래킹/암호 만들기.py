'''
문제
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 
702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 
최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 
또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 
즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 
이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. 
C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 
주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

출력
각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.
'''
import sys
L, C = map(int,sys.stdin.readline().split())
words = list(map(str,sys.stdin.readline().split()))
words.sort()
# 최소 한 개의 모음, 두 개의 자음

arr = [0 for _ in range(15)]
is_used = [0 for _ in range(15)]
result = []
def dec(k):
    if k == L:
        vo_count = 0
        con_count = 0
        for i in range(L):
            if arr[i] == 'a' or arr[i] == 'e' or arr[i] == 'i' or arr[i] == 'o' or arr[i] == 'u':
                vo_count += 1
            else:
                con_count += 1
        if vo_count < 1 or con_count < 2:
            return
        for i in range(L):
            print(arr[i],end="")
        print()
        return
    for i in range(C):
        if not is_used[i]:
            arr[k] = words[i]
            if k > 0 and ord(arr[k-1]) > ord(arr[k]):
                continue
            is_used[i] = 1
            dec(k+1)
            is_used[i] = 0
dec(0)

'''
입력
3 5
a e i b c

답
abc
bce
bci
입력
3 7
a e i o u b c

정답
abc
bce
bci
bco
bcu
예제 입력 1 
4 6
a t c i s w
예제 출력 1 
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
'''