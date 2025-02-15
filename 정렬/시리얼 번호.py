'''
문제
다솜이는 기타를 많이 가지고 있다. 그리고 각각의 기타는 모두 다른 시리얼 번호를 가지고 있다. 
다솜이는 기타를 빨리 찾아서 빨리 사람들에게 연주해주기 위해서 기타를 시리얼 번호 순서대로 정렬하고자 한다.

모든 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)로 이루어져 있다.

시리얼번호 A가 시리얼번호 B의 앞에 오는 경우는 다음과 같다.

1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
2. 만약 서로 길이가 같다면, 
A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
3. 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.

시리얼이 주어졌을 때, 정렬해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 기타의 개수 N이 주어진다. N은 50보다 작거나 같다. 둘째 줄부터 N개의 줄에 시리얼 번호가 하나씩 주어진다. 
시리얼 번호의 길이는 최대 50이고, 알파벳 대문자 또는 숫자로만 이루어져 있다. 시리얼 번호는 중복되지 않는다.

출력
첫째 줄부터 차례대로 N개의 줄에 한줄에 하나씩 시리얼 번호를 정렬한 결과를 출력한다.
'''
import sys
N = int(sys.stdin.readline())
srl = []
for i in range(N):
    srl.append(list(map(str,sys.stdin.readline().strip())))

# sort에서 lambda사용, 여러 개의 key 사용
srl.sort(key = lambda x : (len(x), sum([int(i) for i in x if i.isdigit()]), "".join(map(str,x))))
# key1: 시리얼 번호 길이 순 정렬
# key2: 시리얼 번호에서 숫자만 더한 값을 기준으로 정렬 (isdigit()은 문자인 숫자('1')를 의미)
# key3: 리스트로 이루어진(['A','B','C','D']) 시리얼 번호를 문자열(['ABCD'])로 만든 후 사전순으로 비교 

for i in srl:
    print("".join(map(str,i)))

'''
예제 입력 1 
5
ABCD
145C
A
A910
Z321
예제 출력 1 
A
ABCD
Z321
145C
A910
예제 입력 2 
2
Z19
Z20
예제 출력 2 
Z20
Z19
예제 입력 3 
4
34H2BJS6N
PIM12MD7RCOLWW09
PYF1J14TF
FIPJOTEA5
예제 출력 3 
FIPJOTEA5
PYF1J14TF
34H2BJS6N
PIM12MD7RCOLWW09
예제 입력 4 
5
ABCDE
BCDEF
ABCDA
BAAAA
ACAAA
예제 출력 4 
ABCDA
ABCDE
ACAAA
BAAAA
BCDEF
'''