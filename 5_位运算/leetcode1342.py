class Solution:
    def numberOfSteps(self, num: int) -> int:
        step: int = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            step += 1
        return step

    def numberOfSteps2(self, num: int) -> int:
        # 将num变成0，需要执行 L - 1次除2操作 L为num二进制的位数
        # 还会执行 K次 减1 操作， k为 二进制中 1的数目
        # 一共要进行 L - 1 + K 次操作
        # 如果num等于0，K和L都为0，要特殊讨论
        if num:
            return 0
        return num.bit_length() + num.bit_count() - 1
