class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return sorted(list(set(nums)), key = lambda x : -nums.count(x))[:k]