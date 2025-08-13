from typing import List

"""
2 <= letters.length <= 104
letters[i] 是一个小写字母
letters 按非递减顺序排序
letters 最少包含两个不同的字母
target 是一个小写字母
"""


class Solution:
    def lower_bound(self, letters: List[str], target: str) -> int:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left_bound = self.lower_bound(letters, chr(ord(target) + 1))
        if left_bound == len(letters):
            return letters[0]
        return letters[left_bound]


# 直接查找target + 1字符在letters中的位置，也就是left_bound，找到了直接返回就好
# 如果没找到，那么left_bound就是target + 1应该插入的位置，那么现在处于target + 1的位置一定是大于target的最小字符
a = Solution().nextGreatestLetter(["x", "x", "y", "y"], "z")
print(a)
a = Solution().nextGreatestLetter(["c", "f", "j"], "j")
print(a)
