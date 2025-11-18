class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new=[]
        for i, v in enumerate(operations):
            if v == "C":
                new.pop()
            elif v == "D":
                new.append(new[-1]*2)
            elif v == "+":
                new.append(new[-1]+new[-2])
            else:
                new.append(int(v))
        return sum(new)


        