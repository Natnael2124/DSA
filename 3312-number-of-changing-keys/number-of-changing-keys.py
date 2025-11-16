class Solution:
    def countKeyChanges(self, s: str) -> int:
        result=0
        for i in range(len(s)-1):
            if s[i].lower()!= s[i+1].lower():
                result += 1
        return result

                

        