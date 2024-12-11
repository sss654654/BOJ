```python
>>> from collections import deque
>>> d = deque([1,2,3,4,5])
>>> d.append(6)
>>> d
deque([1, 2, 3, 4, 5, 6])
>>> d.appendleft(0)
>>> d
deque([0, 1, 2, 3, 4, 5, 6])
>>> d.pop()
6
>>> d
deque([0, 1, 2, 3, 4, 5])
>>> d.popleft()
0
>>> d
deque([1, 2, 3, 4, 5])
>>>
```