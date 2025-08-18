class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ## 按位异或： 不同为1，相同为0，刚好满足汉明距离
        return (x ^ y).bit_count()
