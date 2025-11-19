class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l=[]
        arr_set= set(arr)
        for n in range(1,1000000):
            if k==0:
                return l[-1]

            elif n not in arr_set:
                k-=1
                l.append(n)
            
        