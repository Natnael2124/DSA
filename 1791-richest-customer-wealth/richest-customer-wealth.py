class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        acc=0
        for l in accounts:
            s = sum(l)
            if s >acc:
                acc = s
        return acc
            
        