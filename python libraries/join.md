# Join

---

### 기본적으로 문자열로 이루어진 리스트만 가능

```python
arr1 = ['a', 'b', 'c', 'd']
print(', '.join(arr1))

출력 결과: a, b, c, d
```

```python
a = ['is', 'you', 'down']
print('_'.join(a))
print(' '.join(a))

출력결과:
is_you_down
is you down
```
---


### int리스트는 map을 사용해서 해결

```python
arr2 = [1, 2, 3 ,4]
print(', '.join(map(str,arr2)))

출력결과:
1, 2, 3, 4
```
---

### 응용

```python
arr2 = [1, 2, 3 ,4]
print("<%s>" %(', '.join(map(str,arr2))))

출력결과:
<1, 2, 3, 4>
```
---