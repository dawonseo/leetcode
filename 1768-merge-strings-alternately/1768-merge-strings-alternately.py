class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ["" for _ in range(max(len(word1), len(word2)) * 2)]
        
        for i in range(len(word1)):
            ans[i * 2] = word1[i]
            
        for i in range(len(word2)):
            ans[i * 2 + 1] = word2[i]
            
        return "".join(ans)