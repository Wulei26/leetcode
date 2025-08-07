from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        ## 新建一个数组
        ans = [0] * n
        # 第一次的右端点
        rp = k + 1 if k > 0 else n
        ##初始和
        init_sum = sum(code[rp - abs(k) : rp])
        for i in range(n):
            ans[i] = init_sum
            init_sum += code[rp % n] - code[(rp - abs(k)) % n]
            rp += 1
        return ans


if __name__ == "__main__":
    a = Solution().decrypt([5, 7, 1, 4], 3)
    print(a)
