import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ## 如果能成为2的幂， 那么这个数的二进制 一定是 1 10 100 10000 这样的数
        ## 而且负数一定不能成为 2 的幂
        return n.bit_count() == 1 and n > 0

    def isPowerOfTwo2(self, n: int) -> bool:
        ## 如果能成为2的幂， 那么这个数的二进制 一定是 1 10 100 10000 这样的数
        ## 而且负数一定不能成为 2 的幂
        return n > 0 and (math.log10(n) / math.log10(2)) % 1 == 0
