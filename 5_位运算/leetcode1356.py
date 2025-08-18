from typing import List
from functools import cmp_to_key


class Solution:
    def custom_compare(self, a: int, b: int) -> int:
        if a.bit_count() == b.bit_count():
            return a - b
        return a.bit_count() - b.bit_count()

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=cmp_to_key(self.custom_compare))


if __name__ == "__main__":
    a = Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(a)
    a = Solution().sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])
    print(a)
