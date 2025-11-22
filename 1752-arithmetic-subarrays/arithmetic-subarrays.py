class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        
        for left, right in zip(l, r):
            sub = nums[left:right+1]
            sub.sort()
            
            diff = sub[1] - sub[0]
            valid = True
            
            for i in range(2, len(sub)):
                if sub[i] - sub[i-1] != diff:
                    valid = False
                    break
            
            ans.append(valid)
        
        return ans