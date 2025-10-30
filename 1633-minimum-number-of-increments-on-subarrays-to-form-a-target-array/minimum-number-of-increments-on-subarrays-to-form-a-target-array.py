class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        operations = target[0]  # start with first element
        for i in range(1, len(target)):
            operations += max(0, target[i] - target[i-1])
        return operations

