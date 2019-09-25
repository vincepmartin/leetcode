# Definition for singly-linked list.
class Pqueue(object):
    def __init__(self):
        self.maxItem = None
        self.store = {}

    def peek(self):
        return self.maxItem

    def add(self, item):
        if item in self.store:
            self.store[item] += 1
            
        else:
            self.store[item] = 1

        if self.maxItem is None:
            self.maxItem = item
        
        else:
            if self.store[item] > self.store[self.maxItem]:
                self.maxItem = item

    def findMaxItem(self):
        self.maxItem = None
        for k,v in self.store.items():

            if self.maxItem == None:
                self.maxItem = k 

            else:
                if v > self.store[self.maxItem]:
                    self.maxItem = k 

    # Pop the max value and recalc the new max.
    def pop(self):
        temp = self.maxItem
        del self.store[self.maxItem]
        self.findMaxItem()
        return temp

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = Pqueue()

        # Create our priority queue and add values...
        for i in nums:
            pq.add(i)

        kItems = []
        for i in range(0, k):
            kItems.append(pq.pop())

        return kItems

s = Solution()
t1 = [1,1,1,2,2,3] 
k1 = 2

print(s.topKFrequent(t1,k1))
