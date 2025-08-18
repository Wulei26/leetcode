import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (math.log10(n) / math.log10(4)) % 1 == 0
