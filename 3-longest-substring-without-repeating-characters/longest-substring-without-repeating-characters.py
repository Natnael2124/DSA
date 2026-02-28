class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        j=0
        i=0
        collect=set()
        current=0
        
        while j < len(s):
        
            if s[j] not in collect:
                collect.add(s[j])
                j+=1
                current+=1
            else:
                
                current=j-i-1
                collect.remove(s[i])
                i+=1
                
                
            if length < current:
                length=current
        return length

                