class Solution:
    def binaryGap(self, n: int) -> int:
        ## 不断获取n的最小二进制位
        N = n.bit_length()
        last = -1
        i = 0
        ans = 0
        for i in range(N):
            if n & 1 == 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
            n = n >> 1
        return ans
