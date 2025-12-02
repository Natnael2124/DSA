class Solution:
    def isValid(self, s: str) -> bool:
       hashmap={")":"(","]":"[","}":"{"}
       stack=[]

       for ch in s:
        if ch not in hashmap:
            stack.append(ch)
        else:
            if not stack:
                return False
            else:
                popped = stack.pop()
                if popped!=hashmap[ch]:
                    return False
       return not stack

