class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        myset = set(nums)
        num=[]
        for i in range(1,len(nums)+1):
            if i not in myset:
                num.append(i)
        return num