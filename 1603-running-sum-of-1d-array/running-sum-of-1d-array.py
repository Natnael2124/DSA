class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nu=[]
        for i in range(len(nums)):
            nu.append(sum(nums[0:i+1]))
        return nu
        