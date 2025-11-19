class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)

        for n in range(1, 5000):  
            if n not in arr_set:
                k -= 1
                if k == 0:
                    return n
        