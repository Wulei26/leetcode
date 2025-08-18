class Solution:
    ## 返回 ≥n 的全为 1 的二进制数。
    ## 计算 n 的二进制长度 m，返回长为 m 的全为 1 的二进制数，也就是
    def smallestNumber(self, n: int) -> int:
        """
        1 << n.bit_length() 等价于 2^n.bit_length()
        """
        return (1 << n.bit_length()) - 1
