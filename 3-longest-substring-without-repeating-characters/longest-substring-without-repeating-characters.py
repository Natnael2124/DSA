class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        seet=set()
        n=len(s)

        for r in range(n):
            while s[r] in seet:
                seet.remove(s[l])
                l+=1
            seet.add(s[r])
            w=(r-l)+1
            longest=max(longest,w)

        return longest
