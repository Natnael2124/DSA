class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]  # first row

        for i in range(1, numRows):
            prev = res[-1]
            row = [1]  # first element
            
            # middle elements
            for j in range(1, i):
                row.append(prev[j-1] + prev[j])
            
            row.append(1)  # last element
            res.append(row)
        
        return res