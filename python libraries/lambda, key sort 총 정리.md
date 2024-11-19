# 람다, 람다 사용 key 정렬

## 람다(lambda)

#### 의미 

익명함수를 지칭하는 용어 이말의 뜻은 바로 정의하여 사용할 수 있는 함수

#### 형식 

lambda 인자 : 표현식

#### 람다 함수에 인자를 넣어 사용
```
print((lambda x : x+10)(1))
> 11
```

#### 람다 사용 조건문(if)
```
cheak_pass = lambda x: 'pass' if x >= 70 else 'fail'
```

## 정렬(sort)과 람다(lambda)

파이썬에서 사용하는 sort함수는 key인자를 정하지 않고 사용해오는 것이 보통이다.

EX) 
```
a = [[0,3][1,8][2,0]]
a.sort()
print(a)
>[[0,3][1,8][2,0]]
```

<br/>

sort의 key 인자에 함수를 넘겨줄 경우 우선순위가 정해진다.

아래의 EX2에서는 정수형 배열에서 sort의 기본 key값을 인덱스 1로 정했으므로 정렬 결과가 바뀌는 것이 확인이 가능하다.

EX1) 
```
a = [[0,3][1,8][2,0]]
a.sort(key = lambda x : x[0])
print(a)
>[[0,3][1,8][2,0]]
```
EX2) 
```
a = [[0,3][1,8][2,0]]
a.sort(key = lambda x : x[1])
print(a)
>[[2,0][0,3][1,8]]
```

<br/>

람다의 응용으로 서로 다른 길이가 담겨있는 문자열 배열에서도 문자열 길이 순서대로 '사전형 비교'가 가능하다.

EX1)
```
data_list = ['but','i','wont','hesitate','no','more','no','more','it','cannot','wait','im','yours']
data_list.sort(key=lambda x : len(x))

print(data_list)
>	['i', 'no', 'no', 'it', 'im', 'but', 'wont', 'more', 'more', 'wait', 'yours', 'cannot', 'hesitate']
```

아래는 정수형 배열의 정수들을 문자열로 변경하여 대수비교를 하여 가장 큰 수를 구하는 예제에서의 람다 사용의 예이다.

정수형 배열의 각 요소가 1000을 넘어가지 않는다고 설정할 경우 각 요소 X는 자신을 세번 곱하여 세자리 수까지를 요소로 생각하며 정렬을 진행한다.

EX2)
```
data_list = [3, 30, 34, 5, 9]
data_list.sort(key=lambda x: x*3, reverse = True)

print(data_list)
>	['9', '5', '34', '3', '30']
```

sort(key=lambda x: x*3)의 문장에서

x는 배열의 요소에 따라서 다음과 같은 값들을 세자리 수 까지 비교한다.

333
303/030
343/434
555
999

그 다음 대수비교를 통해 정렬을 진행한다.
