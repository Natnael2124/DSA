class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        dup_less=[nums[0]]
        for n in nums:
            if n!=dup_less[-1]:
                dup_less.append(n)

        count = 0
        for i in range(1,len(dup_less)-1):
            if dup_less[i]>dup_less[i-1] and dup_less[i]>dup_less[i+1]:
                count+=1
            elif dup_less[i]<dup_less[i-1] and dup_less[i]<dup_less[i+1]:
                count+=1
        return count
        