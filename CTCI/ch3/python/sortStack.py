'''
    write an algorithm to sort a stack with the smallest items on top
    an additonal temp stack can be used
'''

class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def peek(self):
		return self.items[len(self.items)-1]

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


def sortStack(stack):
    temp_stack = Stack()
    while not stack.isEmpty():
        stack_top = stack.pop()

        while not temp_stack.isEmpty() and temp_stack.peek() < stack_top:
            temp_top = temp_stack.pop()
            stack.push(temp_top)

        temp_stack.push(stack_top)

        while not stack.isEmpty() and stack.peek() <= temp_stack.peek():
            stack_top = stack.pop()
            temp_stack.push(stack_top)
        
    return temp_stack

s = Stack()

s.push(3)
s.push(4)
s.push(1)
s.push(10)
s.push(8)
s.push(15)
s.push(100)

s = sortStack(s)

for i in range(s.size()):
    print(s.pop())

# output:
#         1
#         3
#         4
#         8
#         10
#         15
#         100