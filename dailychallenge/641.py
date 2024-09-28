class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.limit = k
        self.queue = []
        self.i = -1

    def insertFront(self, value: int) -> bool:
        if not self.size == self.limit:
            if not self.i == self.size - 1:
                self.queue.insert(self.i, value)
                # do not increase i here
                if self.i == -1:
                    self.i += 1
                self.size += 1
                return True
            
            self.queue.insert(self.i, value)
            # do not increase i here
            if self.i == -1:
                self.i = 0
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.size == self.limit:
            if not self.i == 0:
                self.queue.insert(self.i, value)
                self.i += 1
                self.size += 1
                return True
            
            self.queue.insert(0, value)
            self.i += 1
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False

        self.queue.pop(self.i)

        if self.i == self.size - 1:
            self.i = 0
        
        self.size -= 1

        if self.size == 0:
            self.i = -1

        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False

        if not self.i == 0:
            self.queue.pop(self.i - 1)
            self.i -= 1
            self.size -= 1

            if self.size == 0:
                self.i = -1

            return True

        self.queue.pop(self.size - 1)
        self.size -= 1

        if self.size == 0:
            self.i = -1

        return True
        

    def getFront(self) -> int:
        if self.size == 0:
            return -1

        return self.queue[self.i]

    def getRear(self) -> int:
        if self.size == 0:
            return -1

        if not self.i == 0:
            return self.queue[self.i - 1]
        
        return self.queue[self.size - 1]

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.limit


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()