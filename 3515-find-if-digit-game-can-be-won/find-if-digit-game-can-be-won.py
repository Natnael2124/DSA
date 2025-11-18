class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        two = 0 
        one = 0
        for i in nums:
            if i < 10:
                one += i
            else:
                two += i
        return two != one