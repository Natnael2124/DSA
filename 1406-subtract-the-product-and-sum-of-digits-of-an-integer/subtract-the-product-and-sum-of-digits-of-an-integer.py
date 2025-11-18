class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = 0
        m = 1
        while n > 0:
            digit = n % 10
            a += digit
            m *= digit
            n //= 10
        return m - a

