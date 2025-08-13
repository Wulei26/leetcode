from typing import List
from collections import defaultdict


class RangeFreqQuery:
    def lower_bond(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def __init__(self, arr: List[int]):
        indexMap = defaultdict(list)
        for i, x in enumerate(arr):
            indexMap[x].append(i)  ## 这个索引列表一定是单调增加的
        self.indexMap = indexMap

    def query(self, left: int, right: int, value: int) -> int:
        nums = self.indexMap[value]  ## 其中 nums 是value在原数组中的下标
        ## 那么只需要看nums有多少处于[left, right]之中的
        x1 = self.lower_bond(nums, left)  ##第一个大于等于left的下标
        x2 = self.lower_bond(nums, right + 1)  ## 第一个大于right的下标
        return x2 - x1


if __name__ == "__main__":
    a = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
    print(a.query(1, 2, 4))
    print(a.query(0, 11, 33))

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
