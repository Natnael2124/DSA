class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s =str(n)
        a=0
        m=1
        for i in s:
            a+=int(i)
            m*=int(i)
        return m-a

