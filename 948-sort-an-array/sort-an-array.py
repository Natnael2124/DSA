class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        def sortr(l_half, r_half):
            i = 0
            j = 0

            ans = []
            while i < len(l_half) and j < len(r_half):
                if l_half[i] <= r_half[j]:
                    ans.append(l_half[i])
                    i += 1
                else:
                    ans.append(r_half[j])
                    j += 1
            ans.extend(l_half[i:])
            ans.extend(r_half[j:])
        
            return ans
        def merg(l, r, arr):
            if l == r:
                return [arr[l]]
            
            mid = l + (r - l) // 2
            l_half = merg(l, mid, arr)
            r_half = merg(mid + 1, r, arr)

            return sortr(l_half, r_half)    

        l = 0
        r = len(nums) - 1
        return merg(l, r, nums)
        