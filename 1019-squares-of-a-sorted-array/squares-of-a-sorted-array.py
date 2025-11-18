class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new=[]
        for i in nums:
            x=pow(i,2)
            new.append(x)
        new.sort()
        return new

        