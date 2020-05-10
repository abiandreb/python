class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


s = Stack()
s.push('test')
s.push('test2')
print(s.pop())
print(s.size())
print(s.isEmpty())


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue('cat')
q.enqueue('dog')
q.enqueue('hamster')
print(q.size())
print(q.isEmpty())
print(q.dequeue())

