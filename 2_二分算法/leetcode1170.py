from typing import List


class Solution:
    def cal_f_value(self, s: str) -> int:
        ## 计算words的 f值
        nums = [0] * 26
        for i in range(len(s)):
            nums[ord(s[i]) - 97] += 1
        for i in nums:
            if i != 0:
                return i

    def lower_bond(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # queries[i][j]、words[i][j] 都由小写英文字母组成
        # 计算words的f值，存在数组中
        nums = [self.cal_f_value(i) for i in words]
        nums = sorted(nums)  ##排序
        m = len(nums)
        n = len(queries)
        ans = [0] * n
        for i in range(len(queries)):
            fq = self.cal_f_value(queries[i])
            ##将fq在words中查找
            fqindex = self.lower_bond(
                nums, fq + 1
            )  ##这样处理就从 fq<  转换为fq + 1 <= ,刚好可以继续用二分
            ans[i] = m - fqindex
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.numSmallerByFrequency(["cbd"], ["zaaaz"]))
    a = Solution()
    print(a.numSmallerByFrequency(["bbb", "cc"], ["a", "aa", "aaa", "aaaa"]))
