from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n-1, -1, -1):
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]:
                st.pop()
            if st: ## st不为空
                ans[i] = st[-1] - i 
                st.append(i)
        return ans
class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = [] 
        for i in range(n):
            t = temperatures[i]
            while st and t > temperatures[st[-1]]:
                j  = st.pop()
                ans[j] = i - j
            st.append(i)
        return ans
###从右往左遍历
    
# if __name__=='__main__':
#     a = Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
#     print(a)
#     a = Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
#     print(a)
#     a = Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
#     print(a)