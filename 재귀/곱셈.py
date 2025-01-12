'''
문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
'''
import sys
sys.setrecursionlimit(10**9)
A,B,C = map(int, sys.stdin.readline().split())

def mul(a,b,c): # 10 11 12
    # (a^b) % c
    # 12^58 = 4(mod 67) -> 12^116 = 16(mod 67)
    # 1승을 계산할 수 있다. -> k승을 계산했으면 2k승과 2k+1승도 O(1)에 계산할 수 있다
    
    if b == 1: # base condition
        return a%c
    val = mul(a,int(b/2),c)
    val = val*val%c # 
    if b%2 == 0: # 거듭제곱이 짝수면 그대로 값 반환 
        return val
    return val*a%c # 거듭제곱이 홀수면 a를 다시 곱한 뒤 c로 나눈 나머지 반환 
print(mul(A,B,C))
# 10 1 12 -> if b == 1: return val(10%12) = 10(10^1%12)
# 10 2 12 -> if b%2 == 0: return val*val%c(10*10%12) = 4(10^2%12)
# 10 5 12 -> if b%2 != 0: return val*a%c(4*10%12) = 4(10^2%12)*10%12

'''
mul(5,14,3) -> mul(5,7,3) -> mul(5,3,3)=val*a%c(1*5%3=2) -> mul(5,1,3)=a%c(5%3=2)
'''

'''
예제 입력 1 
10 11 12
예제 출력 1 
4
'''