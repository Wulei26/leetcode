from typing import List
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0]* ( n - k + 1)
        windows = sortList([])
        for i in range(n):
            v = nums[i]
            windows.append(v)
            if i < k - 1:
                continue
            if windows[x-1] < 0:
                ans[i - k + 1] = windows[x-1]
            else:
                ans[i - k + 1] = 0
            ##离开窗口
            windows.remove(nums[i - k + 1])
        return ans
            

##用列表实现一个有序队列

class sortList(object):
    def __init__(self, lst: List[int]) -> None:
        self.lst = lst
    def __searchInsert(self,lst: List[int],target: int) -> int:
        left = 0
        right = len(lst) - 1
        while left <= right:
            mid = (right + left ) // 2 # 向下取整
            if lst[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    def append(self, num: int) :
        if self.lst == None:
            raise NameError('List is None!!')
        if len(self.lst) == 0:
            self.lst.append(num)
            return
        ##按照从小到大的顺序排序，使用二分法查找第一个大于num的元素的索引

        self.lst.insert(self.__searchInsert(self.lst, num), num)
    def __getitem__(self, index: int) -> int:
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        if not self.lst:
            raise IndexError("List is empty")
        if index < 0 or index >= len(self.lst):
            raise IndexError(f"Index {index} out of range [0, {len(self.lst)-1}]")
        if index < 0:
            index = len(self.lst) + index
        return self.lst[index]

    def __delitem__(self,index: int) -> None:
        del self.lst[index]

    def remove(self, value: int) -> None:
        self.lst.remove(value)

    def __len__(self) -> int:
        return len(self.lst)
    def __str__(self) -> str:
        return str(self.lst)

if __name__=='__main__':
    # a = sortList([])
    # a.append(1)
    # a.append(2)
    # a.append(2)
    # a.append(5)
    # a.append(0)
    # a.remove(2)
    # print(a)
    a = Solution().getSubarrayBeauty([-3,1,2,-3,0,-3],2,1)
    print(a)

        