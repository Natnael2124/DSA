class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
    
        while nums:
            # Alice removes minimum
            alice_pick = min(nums)
            nums.remove(alice_pick)
            
            # Bob removes minimum
            bob_pick = min(nums)
            nums.remove(bob_pick)
            
            # Append to arr: Bob first, Alice next
            arr.append(bob_pick)
            arr.append(alice_pick)
            
        return arr
            