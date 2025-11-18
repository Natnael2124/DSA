class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new=[]
        for i in nums:
            new.append(pow(i,2))
        new.sort()
        return new

        