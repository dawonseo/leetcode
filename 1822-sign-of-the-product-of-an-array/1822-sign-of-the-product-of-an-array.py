class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cnt = 0
        nums.sort()
        
        for num in nums:
            if num < 0:
                cnt += 1
            elif num == 0:
                return 0
            else:
                break
        
        if cnt % 2 == 0:
            return 1
        else:
            return -1