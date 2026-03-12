class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[i] += i
        if len(nums) == 1:
            return True
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                if i == len(nums)-1 and any(nums.index(num) < i and num >= i for num in  nums):
                    continue
                elif any(nums.index(num) < i and num > i for num in  nums):
                    continue
                else:
                    return False
            else:
                continue
        return True

