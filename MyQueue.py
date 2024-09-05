class MyQueue:
    def __init__(self, mode):
        self.mode = mode
        self.stackDequeue = []
        self.stackQueue = []

    def push(self, value):
        if self.mode == "queue":
            self.stackQueue.append(value)
        else:
            for i in range(len(self.stackDequeue)):
                self.stackQueue.append(self.stackDequeue.pop())
            
            self.stackQueue.append(value)
            self.mode = "queue"

    def pop(self):
        if self.mode == "dequeue":
            self.stackDequeue.pop()
        else:
            for i in range(len(self.stackQueue)):
                self.stackDequeue.append(self.stackQueue.pop())

            self.stackDequeue.pop()
            self.mode = "dequeue"

