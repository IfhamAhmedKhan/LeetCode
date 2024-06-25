class MyQueue(object):

    def __init__(self):
        self.values = []

    def push(self, x):
        self.values.append(x)

    def pop(self):
        return self.values.pop(0) if not self.empty() else None

    def peek(self):
        return self.values[0] if not self.empty() else None

    def empty(self):
        return len(self.values) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()