class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def sub(start,num):
            res.append(num[:])

            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                num.append(nums[i])
                sub(i + 1,num)
                num.pop()
                

        sub(0,[])
        
        return res
