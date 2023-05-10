class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        visited = [[False for _ in range(n)] for _ in range(n)]
        ans = [[0 for _ in range(n)] for _ in range(n)]
        
        cnt = 1
        i = 0
        j = 0
        
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        cur = 0
        
        while cnt <= n ** 2:
            ans[i][j] = cnt
            visited[i][j] = True
            
            if (i + dy[cur]) == -1 or (j + dx[cur]) == -1 or  (i + dy[cur]) == n or (j + dx[cur]) == n:
                cur = (cur + 1) % 4
            elif visited[i + dy[cur]][j + dx[cur]]:
                cur = (cur + 1) % 4
                
            i += dy[cur]
            j += dx[cur]
            cnt += 1
            
        return ans
            