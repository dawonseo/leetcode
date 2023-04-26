class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            for i in str(num):
                s += int(i)
            num = s
        return num
        