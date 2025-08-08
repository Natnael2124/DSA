class Solution:
    def soupServings(self, n: int) -> float:
        from functools import lru_cache

        if n >= 5000:
            return 1.0  # For large n, the result is nearly 1
        
        n = (n + 24) // 25  # Convert mL into units of 25, round up

        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5  # Both become empty
            if a <= 0:
                return 1.0  # A is empty first
            if b <= 0:
                return 0.0  # B is empty first

            return 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )

        return dp(n, n)

        