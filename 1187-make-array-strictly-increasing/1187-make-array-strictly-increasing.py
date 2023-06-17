class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {}
        arr2.sort()
        
        def dfs(prev, i):
            if i >= len(arr1):
                return 0
            if (prev, i) in dp:
                return dp[(prev, i)]

            cost = float('inf')

            if arr1[i] > prev:
                cost = dfs(arr1[i], i + 1)

            idx = bisect.bisect_right(arr2, prev)

            if idx < len(arr2):
                cost = min(cost, 1 + dfs(arr2[idx], i + 1))

            dp[(prev, i)] = cost
            return cost

        dfs(-1, 0)

        return dp[(-1, 0)] if dp[(-1, 0)] < float('inf') else -1
