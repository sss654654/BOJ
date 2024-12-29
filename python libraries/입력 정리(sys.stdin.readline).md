# input()대신 sys.stdin.readline()을 사용하는 이유

한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야 할 때는 input()으로 입력 받는다면 시간초과가 발생할 수 있다.

이러한 이유는 input()은 입력받은 값의 개행문자를 삭제한 뒤(시간초과의 이유) 반환해주지만 sys.stdin.readline()은 개행문자를 포함하여 '문자열'로 반환해주기 때문이다.

<br/>


## 한개의 정수를 입력받을 때

```python
import sys
a = int(sys.stdin.readline())
```

sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아진다.

또한 str로 저장되기 때문에 int로 형변환을 시켜야 한다.

<br/>


## 정해진 개수의 정수를 한줄에 입력받을 때(3개)

```python
import sys
a,b,c = map(int,sys.stdin.readline().split())
```

map()은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수이다.

<br/>


## 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때

```python
import sys
data = list(map(int,sys.stdin.readline().split()))
```

<br/>

## 임의의 숫자 문자열(110101)을 입력받아 따로따로 띄워서 숫자 리스트로 저장할 때

```python
import sys
data = []
data.append(list(map(int,sys.stdin.readline().split())))
```

<br/>

## 문자열 n줄을 입력받아 리스트에 저장할 때

```python
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
# strip()은 문자열 맨 앞과 맨 끝의 공백 문자를 제거
```

<br/>

## 1 1 0 1 1 -> [1,1,0,1,1]

```python
list(map(int,sys.stdin.readline().split()))
```

<br/>

## 11011 -> [1,1,0,1,1]

```python
list(map(int,sys.stdin.readline().strip()))
```