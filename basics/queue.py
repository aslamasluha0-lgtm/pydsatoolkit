from collections import deque
#implementation of queue
q= deque()

#adding a new element to the queue - O(1)
q.append(1)
q.append(2)
q.append(3)

print(q)
#removing an element from the left - O(1)
q.popleft()
print(q)

#peek from the left
print(q[0])

#peek form the right 
print(q[-1])


#using custom class 
class Queue:
    def __init__(self):
        self._items = deque()
    #adding a new element to the queue - O(1)
    def enqueue(self, item):
        self._items.append(item)
    #removing an element from the left - O(1)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()
    #peek from the left
    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]
    #peek form the right 
    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.front())    # 2
print(q.size())     # 2
