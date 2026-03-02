class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runsum=[]
        summ=0
        for i in nums:
            summ+=i
            runsum.append(summ)
        return runsum