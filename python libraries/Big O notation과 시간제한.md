# Big O와 시간제한

흔히 사용하는 Big O notation은 for문은 O(N)이라는 것과 이중 for문은 O(N^2)이라는 것 등이 있다.

하지만 코딩테스트(백준, 프로그래머스) 문제를 풀다보면 시간제한(1초, 2초)등이 확인된다.

<img width="106" alt="image" src="https://user-images.githubusercontent.com/84978165/229667798-07c1f0e8-2257-4aad-8cd7-d3d1e08a9d3a.png">

<br/>

---

시간 제한이 1초인 문제의 경우

<img width="494" alt="image" src="https://user-images.githubusercontent.com/84978165/229668775-36190142-1013-4c87-a4d5-1641ff7f1924.png">

예를 들어 시간 제한이 1초인 문제에서 O(N^2) 즉, 이중 for문으로 문제를 풀고자 할 경우 N이 10000일 때 한번의 루프가 1초가 걸린다는 것이 확인 가능하다. 

N이 10000인 이중 for문이 10번 이상 돌아가면 10초가 걸린다는 말이다.

즉, 문제를 풀이함에 있어서 N이 커짐에 따라서 O(N)이나 O(logN)을 제외하고는 다른 시간복잡도의 알고리즘을 구현하는 것은 어려울 것이다.

<br/>

---

다음의 최대 힙 문제는 시간 제한이 1초이며 N의 범위가 (1 ≤ N ≤ 100,000)이므로 시간 복잡도가 O(logN)인 우선순위 큐(힙)을 사용하여 풀이하는 문제임을 알 수 있었다.

<img width="592" alt="image" src="https://user-images.githubusercontent.com/84978165/229668093-9d4c3155-07b8-4a2e-81df-685f1031de59.png">

<img width="201" alt="image" src="https://user-images.githubusercontent.com/84978165/229668110-2b046d9f-e401-49fa-b7f4-38bc591b538e.png">