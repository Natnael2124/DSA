class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch.isalpha():
                stack.append(ch)
            else:
                stack.pop()
        output="".join(stack)
        return output