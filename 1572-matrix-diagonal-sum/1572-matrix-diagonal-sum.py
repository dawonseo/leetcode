class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        for i in range(n):
            if (n % 2 == 1) and (i == (n // 2)):
                ans += mat[i][i]
            else:
                ans += (mat[i][i] + mat[i][-(i + 1)])
        
        return ans