import sys

N,r,c = map(int,sys.stdin.readline().split())
# 2^N x 2^N

def Z(n,r,c): # n=2,r=3,c=1
    # 4+4+3
    if n == 0:
        return 0
    half = int(2**n / 2) # half = 4
    if r >= half and c >= half: # 4
        return 3*(half**2) + Z(n-1,r-half,c-half)
    elif r >= half and c < half: # 3
        return 2*(half**2) + Z(n-1,r-half,c)
    elif r < half and c >= half: # 3
        return (half**2) + Z(n-1,r,c-half)
    return Z(n-1,r,c)

print(Z(N,r,c))




'''
def Z(n,r,c):
    if n == 0:
        return 0
    half = 2**(n-1) # 2^(n-1)
    if r < half and c < half: # 1
        print(1,r,c)
        return Z(n-1,r,c) # 모든 함수는 1사분면으로 귀결
    if r < half and c >= half: # 2
        print(2,r,c)
        return half*half + Z(n-1,r,c-half) # 모든 함수는 1사분면으로 귀결
    if r >= half and c < half: # 3
        print(3,r,c)
        return 2*half*half + Z(n-1,r-half,c) # 모든 함수는 1사분면으로 귀결
    print(4, r, c)
    return 3*half*half + Z(n-1,r-half,c-half) # 4, 모든 함수는 1사분면으로 귀결
print(Z(N,r,c))
# 3 7 7 -> 48(4)+12(4)+3(4)
# 3 4 4 -> 48(4)+0+0

'''