1. key로만 순회하기

```python
# key로만 순회
dict = {'김철수': 300, 'Anna': 180}
for key in dict:
    print(key)
    # 이 경우 value를 찾고 싶으면 dict[key] 와 같이 접근을 따로 해주어야.

'''
김철수
Anna
'''
```

2. key, value 동시 순회하기 (items() 사용)


```python
# key-value 동시 순회

dict = {'김철수': 300, 'Anna': 180}
for key, value in dict.items():
    print(key, value)

'''
김철수 300
Anna 180
'''

import collections

dict = collections.defaultdict(int)
for i in N:
	dict[i] += 1
print(dict)
# defaultdict(<class 'int'>, {1: 2, 5: 1, 4: 2, 2: 1, 3: 2})

dict_count = collections.Counter(N)
print(dict_count)
# defaultdict(<class 'int'>, {1: 2, 5: 1, 4: 2, 2: 1, 3: 2})

dict_order = collections.OrderedDict(N)
print(dict_order)


```