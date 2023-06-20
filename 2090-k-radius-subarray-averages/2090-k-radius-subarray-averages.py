class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        d = (k * 2) + 1
        ans = [-1 for _ in range(n)]
        if n >= d:
            s = sum(nums[:d])
        else:
            return ans
        
        
        for i in range(k, n - k):
            if i != k:
                s -= nums[i - k - 1]
                s += nums[i + k]
            ans[i] = int(s/d)
        
        return ans
            