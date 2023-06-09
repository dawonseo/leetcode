class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target = int(ord(target))
        if int(ord(letters[-1])) <= target:
            return letters[0]
        
        for i in letters:
            if int(ord(i)) > target:
                return i