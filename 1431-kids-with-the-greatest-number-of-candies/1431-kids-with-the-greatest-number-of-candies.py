class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        m = max(candies) - extraCandies
        ans = [True for _ in range(n)]
        
        for i in range(n):
            if candies[i] < m:
                ans[i] = False
        
        return ans