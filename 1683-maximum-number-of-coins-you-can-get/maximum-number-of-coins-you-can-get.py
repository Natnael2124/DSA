class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
    
        ans = 0
        left = 0
        right = n - 1
    
        for _ in range(n // 3):
            right -= 1          
            ans += piles[right] 
            right -= 1          
            left += 1           

        return ans
        