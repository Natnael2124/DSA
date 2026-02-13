class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d=list(s.split(" "))

        if len(pattern)!=len(d):
            return False

        count_p=Counter(pattern)
        count_d=Counter(d)
        mp={}
        for i in range(len(pattern)):
            if pattern[i] not in mp.keys() and d[i] not in mp.values():
                mp[pattern[i]]=d[i]
            
            if pattern[i] not in mp.keys():
                return False

            elif mp[pattern[i]]!= d[i]:
                return False
        return True
        '''
        for i in range(len(pattern)):
            if count_p[pattern[i]]!=count_d[d[i]] and pat:
                return False
        return True'''
        