class Solution:
    def findComplement(self, num: int) -> int:
        ## 相当于与它相同长度的 全1的二进制数 取 按位异或
        return num ^ ((1 << num.bit_length()) - 1)
