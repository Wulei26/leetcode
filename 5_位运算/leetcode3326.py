class Solution:
    ## https://leetcode.cn/discuss/post/3571304/cong-ji-he-lun-dao-wei-yun-suan-chang-ji-enve/
    def minChanges(self, n: int, k: int) -> int:
        """
        & 表示按位与，∣ 表示按位或，^ 表示按位异或，∼ 表示按位取反
        """
        if n & k != k:
            return -1
        ## 这里说明 k一定是n的子集，那么n的二进制位 为0 的地方，k在其对应的位置也必然为0
        ## 所以要将n变成k， 只需要 n ^ k 按位异或 (两个位不同时结果为 1，相同时结果为 0),因为 k为0的位，n可能为0也可能为1， 如果为0，那么按位异或结果为0，如果为1 结果为1，刚好是将n变成k的操作
        return (n ^ k).bit_count()  ## 统计的是 二进制位中 1 的数量
