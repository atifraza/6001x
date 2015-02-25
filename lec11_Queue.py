class Queue(object):
    def __init__(self):
        self.size = 0
        self.elements = []
    
    def insert(self,e):
        self.size += 1
        self.elements.append(e)
    
    def remove(self):
        if self.size > 0:
            self.size -= 1
            return self.elements.pop(0)
        else:
            raise ValueError("ValueError")

queue = Queue()
queue.insert(5)
queue.insert(6)
queue.remove()
queue.insert(7)
queue.remove()
queue.remove()
queue.remove()