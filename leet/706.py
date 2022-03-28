# Design Hash Map

# hash map 사용법. key 를 가지고 hash function을 사용해 index로 만들어서
# value를 집어넣는다.
from itertools import combinations
import collections
import heapq

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None # linked list, not doubly

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
    
    def put(self, key:int, value:int)->None:
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        head = self.table[index] 
        while head:
            if head.key == key:
                head.value = value
                return
            # 다음 노드가 없으면
            if head.next is None:
                break
            
            head = head.next
        # head 는 일종의 포인터구나 
        # 다음 노드가 없어서 while문을 나왔으므로, 끝에다 만들어줌.
        head.next = ListNode(key, value)
    
    def get(self, key:int)->int:
        index = key % self.size

        if self.table[index].value is None:
            return -1
        
        head = self.table[index]

        while head:
            if head.key == key:
                return head.value
            head = head.next
        return -1
    
    def remove(self, key:int)->None:
        index = key % self.size
        if self.table[index].value is None:
            return 
        
        head = self.table[index]

        if head.key == key:
            # 첫번째 값일때 next가 None이면 빈노드 삽입
            # next가 있으면 head.next 만 하면됨. 
            self.table[index] = ListNode() if head.next is None else head.next
            return
        
        prev = head
        while head:
            if head.key == key:
                # 이전의 다음블록이 지금의 다음블록이 되는것. 
                prev.next = head.next
                return
            # while문에서 움직이기 위함.
            prev, head = head, head.next
