class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


if __name__ == "__main__":
    q = int(input())
    queue = MyQueue()

    for _ in range(q):
        values = input().split()
        if values[0] == "1":
            queue.enqueue(int(values[1]))
        elif values[0] == "2":
            queue.dequeue()
        elif values[0] == "3":
            print(queue.peek())
