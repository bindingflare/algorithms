class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        size = len(self.intervals)

        i = self.binary_search(start)
        #print('i =', i)

        # test start
        #print(self.intervals)
        if i == size:
            self.intervals.insert(i, end)
            self.intervals.insert(i, start)

            return True

        if i % 2 == 0: # is a start
            starting_at = self.intervals[i]

            if i == 0:
                if end <= starting_at:
                    self.intervals.insert(i, end)
                    self.intervals.insert(i, start)

                    return True
            elif start >= self.intervals[i - 1] and end <= starting_at:
                self.intervals.insert(i, end)
                self.intervals.insert(i, start)

                return True
                
        else: # is an end
            ending_at = self.intervals[i]

            i += 1
            if i == size:
                if start >= ending_at:
                    self.intervals.insert(i, end)
                    self.intervals.insert(i, start)

                    return True
            elif start >= ending_at and end <= self.intervals[i]:
                self.intervals.insert(i, end)
                self.intervals.insert(i, start)

                return True
    
        return False

    def binary_search(self, target: int) -> int:
        low = 0
        high = len(self.intervals) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_val = self.intervals[mid]

            # print("mid=", mid)

            if mid_val == target:
                return mid
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1

        return low; # return the last successful search index



        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

###
# class MyCalendar:

#     def __init__(self):
#         self.intervals = []

#     def book(self, start: int, end: int) -> bool:
#         passed = True
#         size = len(self.intervals)

#         # base case
#         if size == 0:
#             self.intervals.append(start)
#             self.intervals.append(end)

#             return True

#         i = self.binary_search(start)
#         #print('i =', i)
#         j = self.binary_search(end)
#         #print('j =', j)

#         if abs(i - j) > 1:
#             return False

#         # test start
#         if not i == size:
#             if i % 2 == 0: # is a start
#                 starting_at = self.intervals[i]

#                 passed = passed and (start < starting_at)
                    
#             else: # is an end
#                 ending_at = self.intervals[i]

#                 passed = passed and (start >= ending_at)
           

#         # test end
#         if not j == size:
#             if j % 2 == 0: # is a start
#                 started = self.intervals[j]

#                 passed = passed and (end <= started)
#             else: # is an end
#                 ended = self.intervals[j]

#                 passed = passed and (end > ended)
        
#         if passed:
#             self.intervals.insert(i, start)
#             self.intervals.insert(j + 1, end)

#             #print(self.intervals)

#         return passed

#     def binary_search(self, target: int) -> int:
#         low = 0
#         high = len(self.intervals) - 1

#         while low <= high:
#             mid = (low + high) // 2
#             mid_val = self.intervals[mid]

#             # print("mid=", mid)

#             if mid_val == target:
#                 return mid
#             elif mid_val < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1

#         return low; # return the last successful search index



        


# # Your MyCalendar object will be instantiated and called as such:
# # obj = MyCalendar()
# # param_1 = obj.book(start,end)
###
obj = MyCalendar()
print(obj.book(10,20))
print(obj.book(15,25))
print(obj.book(20,30))