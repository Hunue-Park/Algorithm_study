# cicular queue

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] *k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int)->bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            # rear pointer (p2) 가리키는 자리에 value를 넣는다.
            self.p2 = (self.p2 + 1) % self.maxlen 
            # 길이 넘어가면 나머지 연산을 통해 원형큐 유지
            return True
        else:
            return False

    def deQueue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self):
        #p1이 가리키는 맨앞의 요소를 반환
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self):
        # p1 과 p2 가 가리키는 자리가 같고, 요소가 없다면 큐는 비어있다. 
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None

