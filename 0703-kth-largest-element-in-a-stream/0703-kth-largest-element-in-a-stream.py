class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.li = []
        self.k = k
        for i in nums:
            self._push(i)
    
    def _push(self, val: int):
        if self.k == len(self.li):
            top = heapq.heappop(self.li)
            if val > top:
                heapq.heappush(self.li, val)
            else:
                heapq.heappush(self.li, top)
        else:
            heapq.heappush(self.li, val)

    def add(self, val: int) -> int:
        self._push(val)
        return self.li[0] if len(self.li) == self.k else None
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)