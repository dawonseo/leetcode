class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        
        for i in letters:
            if i > target:
                return i