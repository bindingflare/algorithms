class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()


class AllOne:
    def __init__(self):
        self.head = Node(0)  # Dummy head
        self.tail = Node(0)  # Dummy tail
        self.head.next = self.tail  # Link dummy head to dummy tail
        self.tail.prev = self.head  # Link dummy tail to dummy head
        self.map = {}  # Mapping from key to its node

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq
            node.keys.remove(key)  # Remove key from current node

            nextNode = node.next
            if nextNode == self.tail or nextNode.freq != freq + 1:
                # Create a new node if next node does not exist or freq is not freq + 1
                newNode = Node(freq + 1)
                newNode.keys.add(key)
                newNode.prev = node
                newNode.next = nextNode
                node.next = newNode
                nextNode.prev = newNode
                self.map[key] = newNode
            else:
                # Increment the existing next node
                nextNode.keys.add(key)
                self.map[key] = nextNode

            # Remove the current node if it has no keys left
            if not node.keys:
                self.removeNode(node)
        else:  # Key does not exist
            firstNode = self.head.next
            if firstNode == self.tail or firstNode.freq > 1:
                # Create a new node
                newNode = Node(1)
                newNode.keys.add(key)
                newNode.prev = self.head
                newNode.next = firstNode
                self.head.next = newNode
                firstNode.prev = newNode
                self.map[key] = newNode
            else:
                firstNode.keys.add(key)
                self.map[key] = firstNode

    def dec(self, key: str) -> None:
        if key not in self.map:
            return  # Key does not exist

        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            # Remove the key from the map if freq is 1
            del self.map[key]
        else:
            prevNode = node.prev
            if prevNode == self.head or prevNode.freq != freq - 1:
                # Create a new node if the previous node does not exist or freq is not freq - 1
                newNode = Node(freq - 1)
                newNode.keys.add(key)
                newNode.prev = prevNode
                newNode.next = node
                prevNode.next = newNode
                node.prev = newNode
                self.map[key] = newNode
            else:
                # Decrement the existing previous node
                prevNode.keys.add(key)
                self.map[key] = prevNode

        # Remove the node if it has no keys left
        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""  # No keys exist
        return next(
            iter(self.tail.prev.keys)
        )  # Return one of the keys from the tail's previous node

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""  # No keys exist
        return next(
            iter(self.head.next.keys)
        )  # Return one of the keys from the head's next node

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode  # Link previous node to next node
        nextNode.prev = prevNode  # Link next node to previous node

# class AllOne:
#     def __init__(self):
#         self.keys = defaultdict(int)
#         self.values = defaultdict(dict)
#         self.counts = defaultdict(int)
#         self.min = 0
#         self.max = 0
#         self.size = 0

#     def inc(self, key: str) -> None:
#         old_val = self.keys[key]
#         new_val = old_val + 1

#         self.keys[key] = new_val

#         self.counts[new_val] += 1

#         if not old_val == 0:
#             del self.values[old_val][key]
#             self.counts[old_val] -= 1
#         else:
#             self.min = 1 # new entry, min will always be 1

#         self.values[new_val][key] = 0

#         if old_val == self.min:
#             # make sure no duplicates exist in the old value
#             if self.counts[old_val] == 0:
#                 self.min += 1
#         if old_val == self.max:
#             # safe to update max without checking
#             self.max += 1

#         self.size += 1
        

#     def dec(self, key: str) -> None:
#         old_val = self.keys[key]
#         new_val = old_val - 1

#         self.keys[key] = new_val

#         self.counts[old_val] -= 1

#         del self.values[old_val][key]

#         self.size -= 1

#         if new_val == 0:
#             del self.keys[key]

#             # do not create new values entry

#             if self.min == 1 and self.counts[old_val] == 0 and not self.size == 0:
#                 # find next min
#                 while self.counts[self.min] == 0:
#                     self.min += 1

#             if self.size == 0:
#                 self.min = 0
#                 self.max = 0
#         else:
#             self.values[new_val][key] = 0

#             self.counts[new_val] += 1

#             if old_val == self.min:
#                 # safe to update min without checking
#                 self.min -= 1
#             if old_val == self.max:
#                 # check duplicates
#                 if self.counts[old_val] == 0:
#                     self.max -= 1

#     def getMaxKey(self) -> str:
#         if self.size == 0:
#             return ""

#         return next(iter(self.values[self.max]))

#     def getMinKey(self) -> str:
#         #print(self.values)
#         #print(self.min)
#         if self.size == 0:
#             return ""

#         return next(iter(self.values[self.min]))
        


# # Your AllOne object will be instantiated and called as such:
# # obj = AllOne()
# # obj.inc(key)
# # obj.dec(key)
# # param_3 = obj.getMaxKey()
# # param_4 = obj.getMinKey()