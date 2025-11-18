class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prodcut = math.prod(nums)
        def signFunc(x):
            if x>0 or x<0:
                p=x//abs(x)
            else:
                p=x
            return p
        return signFunc(prodcut)