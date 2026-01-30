class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            value=0
            for i in str(num):
                value+=int(i)
            num =value
        return num