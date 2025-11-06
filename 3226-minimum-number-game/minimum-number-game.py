class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()
        for i in range(0,len(nums), 2):
            alex_pick=nums[i]
            bob_pick=nums[i+1]
            arr.append(bob_pick)
            arr.append(alex_pick)
        return arr

            