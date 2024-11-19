# 우선순위 큐(Heap)

우선순위 큐 => pop을 할 때 가장 먼저 들어온 원소가 나오는 대신 우선순위가 가장 높은 원소가 나오는 큐

1. 원소의 추가가 O(logN)
2. 우선순위가 가장 높은 원소의 확인이 O(1)
3. 우선순위가 가장 높은 원소의 제거가 O(logN)

최댓 값을 찾기위해 사용하는 힙을 최대 힙, 최솟 값을 찾기위해 사용하는 힙을 최소 힙이라고 한다.

<br/>

### 최소 힙(최대 힙은 반대)

<img width="420" alt="image" src="https://user-images.githubusercontent.com/84978165/229509763-4888a914-4377-47c5-8284-b29992934629.png">

제일 작은 값이 트리의 루트에 위치하는 것이 확인 가능하다.

<br/>

### 최소 힙에서 삽입하는 순서

<img width="398" alt="image" src="https://user-images.githubusercontent.com/84978165/229510012-17c31e88-c93d-456f-b594-98baa6e7ea3d.png">

높이가 낮은 곳부터 채워나가며 높이가 같을 경우에는 왼쪽부터 값을 삽입한다.

<br/>

### (최소)힙 삽입

균형 트리이기 때문에 시간 복잡도는 O(logN)이다.

<img width="255" alt="image" src="https://user-images.githubusercontent.com/84978165/229510673-9e050f9d-3cae-4f62-94c4-a33acfce7679.png">

<img width="255" alt="image" src="https://user-images.githubusercontent.com/84978165/229510712-127eb1f1-eff1-4fa5-9c32-9252e73fd530.png">

<img width="255" alt="image" src="https://user-images.githubusercontent.com/84978165/229510790-ac014138-1fd2-4ba7-a577-f32ea60f52f9.png">

<img width="255" alt="image" src="https://user-images.githubusercontent.com/84978165/229510848-5b408b2e-f7b7-4592-a353-8f5ac349f370.png">


<br/>

### 힙에서 값 가져오기 

최소 힙에서는 최솟값을 빠르게 가져올 수 있으나 열번 째로 작은 값이라던가 최댓값을 가져오기 위해서는 트리를 전부 탐색해야 한다.

최대 힙 또한 마찬가지로 최댓값을 빠르게 가져올 수 있으나 열번 째로 큰 값이라던가 최솟값을 가져오기 위해서는 트리를 전부 탐색해야 한다.

따라서 시간복잡도는 O(1)이다.

<br/>

### (최소)힙에서 원소 제거 

삽입과 마찬가지로 균형 트리이기 때문에 시간 복잡도가 O(logN)이다.

<br/>

<img width="369" alt="image" src="https://user-images.githubusercontent.com/84978165/229511872-7620345f-e7e0-4771-af26-7bdc41cbbb64.png">

힙에서 원소를 제거할 경우에는 트리의 구조가 깨질 수 있으므로 주의해야 한다.

<img width="369" alt="image" src="https://user-images.githubusercontent.com/84978165/229512001-8878e093-787f-4eda-b67c-48fe94129f0a.png">

트리의 구조를 지키기 위해서 최소 힙에서 최솟값과 최댓값의 위치를 바꾼다.

<img width="369" alt="image" src="https://user-images.githubusercontent.com/84978165/229512359-157d8373-c986-4ba2-9934-0fbf426f56cf.png">

최소 힙은 부모가 자식보다 작아야 하는 성질을 지켜야 하므로 12와 13중 작은 값을 상위 레벨의 높은 값과 위치를 바꾼다. 이를 반복하며 원소를 제거해나간다.(여기서 8은 삭제해도 트리의 구조가 깨지지 않으므로 이미 삭제되었음)

<img width="369" alt="image" src="https://user-images.githubusercontent.com/84978165/229512738-057369e0-f970-426a-9580-ceb0c90fe374.png">

비교할 두 값이 같을 경우는 무엇을 올려도 상관없다.

<img width="369" alt="image" src="https://user-images.githubusercontent.com/84978165/229512899-8f302a07-f240-4c78-9282-7361836e642b.png">

<img width="369" alt="image" src="https://user-images.githubusercontent.com/84978165/229512986-30acefa3-110e-47d5-8357-867ad43b9e1f.png">


<br/>

### 우선순위 큐 직접 구현

1번째 인덱스부터 시작한 이유는 x로 식을 세워 생각하기에 편하게 하기 위함(0으로 시작해도 상관은 없어보인다)

<img width="504" alt="image" src="https://user-images.githubusercontent.com/84978165/229513515-3f2c04b8-ce27-4f98-94e7-30a55e2a2a43.png">

```python

# 아래의 코드는 최대 힙을 구현한 것이며 주석에서 언급한 부분의 코드를 바꾸면 최소 힙이 된다.
heap = []
sz = 0

def push(x):
    global sz
    heap.append(x)
    sz += 1
    idx = sz - 1
    while (idx != 0):  # 최댓값의 idx가 0이되면 break
        # print(heap)
        par = int((idx - 1) / 2)
        if heap[par] >= heap[idx]:  # 부모가 자식 노드들 보다 클 경우 이상없음(최대 힙), 반대의 경우는 최소 힙
            break
        temp = heap[par]
        heap[par] = heap[idx]
        heap[idx] = temp
        idx = par  # 최댓값의 idx가 0으로 만들기 위함


def pop():
    global sz
    sz -= 1
    heap[0] = heap[sz]  # 삭제하려는 부분(루트)을 맨 마지막 노드와 바꿈
    heap.pop()
    idx = 0
    while (2*idx + 1 < sz):
        lc = 2*idx + 1
        rc = 2*idx + 2
        max_child = lc
        if rc < sz:  # 오른쪽 노드가 존재한다면
            if heap[rc] > heap[lc]:
                max_child = rc
        if heap[idx] >= heap[max_child]:  # 부모가 자식 노드들 보다 클 경우 이상없음(최대 힙), 반대의 경우는 최소 힙
            break
        temp = heap[max_child]
        heap[max_child] = heap[idx]
        heap[idx] = temp
        idx = max_child


def top():
    return heap[0]
```

<br/>

### 우선순위 큐 라이브러리

python 

```python
from queue import PriorityQueue 

#선언 (최소 힙이 기준)
que = PriorityQueue()

que = PriorityQueue(maxsize=8)

#추가
que.put(4)
que.put(1)
que.put(7)

#삭제
print(que.get())  # 1
print(que.get())  # 4
print(que.get())  # 7

#최소 힙이 아닌 최대 힙을 구현하고자 할 경우
#(우선순위, 값)의 튜플의 형태로 데이터를 추가하고 제거

que.put((-4, 4))
que.put((-1, 1))
que.put((-7, 7))

print(que.get()[1])  # 7
print(que.get()[1])  # 4
print(que.get()[1])  # 1


import heapq

hq = []

heapq.heappush(hq, 4)
heapq.heappush(hq, 1)
heapq.heappush(hq, 3)
heapq.heappush(hq, 7)

heapq.heappop(hq) # 1

x = [4, 3, 1, 2, 5, 6]
print(x) # [4, 3, 1, 2, 5, 6]
heapq.heapify(x)
print(x) # [1, 2, 4, 3, 5, 6]

```

c

```c
#include <iostream>
#include <queue>

using namespace std;
int main() {
    priority_queue<int> pq;
    .
    .
    .
    .
    }
```