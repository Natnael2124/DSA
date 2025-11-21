class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        result = []

        for x in arr2:
            result.extend([x] * freq[x])
            freq[x] = 0  

        for x in sorted(freq.keys()):
            if freq[x] > 0:
                result.extend([x] * freq[x])

        return result
        