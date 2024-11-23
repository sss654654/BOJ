# 단일 연결 리스트

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 노드 생성, 연결
head = ListNode(0)

curr_node = head

new_node = ListNode(1)
curr_node.next = new_node
curr_node=curr_node.next

curr_node.next = ListNode(2)
curr_node=curr_node.next

# 연결 리스트 값 출력
node=head
while node:
    print(node.val)
    node=node.next

# 노드 탐색하여 삭제
node=head
while node.next:
    if node.next.val==2:
        next_node=node.next.next
        node.next=next_node
        break
    node=node.next

# 연결 리스트의 끝에 새 노드를 추가

def addBack(data):
    node = head
    while node:
        if node.next is None:
            node.next = Node(data)
            break
        node = node.next
