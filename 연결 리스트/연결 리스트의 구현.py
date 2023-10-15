# 단일 연결 리스트

class Node():
    def __init__(self,data):
        self.data = None
        self.next = None
        self.prev = None


# 노드 생성, 연결

head = Node(1)
head.next = Node(2)
head.next.next = Node(3) 

# 연결 리스트 값 출력

def printNodes():
    node = head
    while node: # node is not None
        print(node.data, end = " ")
        node = node.next

# 연결 리스트의 끝에 새 노드를 추가

def addBack(data):
    node = head
    while node:
        if node.next is None:
            node.next = Node(data)
            break
        node = node.next
