class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        order = [i for i in range(n)]
        order.sort(key = lambda x: nums[x])
        psum = [0 for _ in range(n + 1)]
        ssum = [0 for _ in range(n + 1)]
        sb1 = [0 for _ in range(n)]
        sb2 = [0 for _ in range(n)]

        for i in range(n):
            psum[i + 1] = psum[i] + cost[order[i]]
            ssum[-(i + 2)] = ssum[-(i + 1)] + cost[order[-(i + 1)]]
            if i != 0:
                sb1[i] += sb1[i - 1] + psum[i] * (nums[order[i]] - nums[order[i - 1]])
                sb2[-(i + 1)] += sb2[-i] + ssum[-(i + 1)]  * (nums[order[-i]] - nums[order[-(i + 1)]])
        
        for i in range(n):
            if (sb1[i] + sb2[i]) < ans:
                ans = sb1[i] + sb2[i]
        
        return ans