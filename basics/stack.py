#stack implementation using dynamic array
stack1 = []

#adding element to end of the stack 
stack1.append(1)
stack1.append(2)
stack1.append(3)

#removing the last element from stack
stack1.pop()

#peek in the stack
print(stack1[-1])

#finding the length of the stack
print(len(stack1))

#using custom class
class Stack:
  def __init__(self):
    self._item=[]
  #adding element to end of the stack 
  def push(self,item):
    self._item.append(item)
  #removing the last element from stack
  def pop(self):
    return self._item.pop()
  #peek in the stack
  def peek(self):
    return self._item[-1]
  def show(self):
    return self._item


stack =Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.show())
    
