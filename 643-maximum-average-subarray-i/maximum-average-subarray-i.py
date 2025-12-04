class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum=sum(nums[:k])
        w=current_sum
        n=len(nums)
        l=0
        
        for r in range(k,n):
            
            current_sum =current_sum+ nums[r]-nums[l]
            l+=1
            w=max(current_sum,w)

        return w/k