class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i=[]
        j=[]
        for ch in s:
            if ch == "#" and  i: 
                i.pop()
            elif ch != "#":
                i.append(ch)
        for ch in t:
            if ch == "#" and j:
                j.pop()
            elif ch != "#":
                j.append(ch)
        return i == j

