class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        cnt = 0
        ans = 0
        
        for i in range(k):
            cnt += int(s[i] in vowels)
        
        ans = cnt
        
        for j in range(k, len(s)):
            cnt += int(s[j] in vowels)
            cnt -= int(s[j - k] in vowels)
            ans = max(ans, cnt)
            
        return ans