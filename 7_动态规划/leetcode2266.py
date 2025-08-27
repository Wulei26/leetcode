from itertools import groupby
class Solution:

    def countTexts(self, pressedKeys: str) -> int:
        mod= 10 ** 9 + 7
        ##对于23456 8 来说 ，如果连续按某个数字 这里以2举例
        #按一次 只能是a
        #按2次 a或者aa
        ##按三次，可能是 aaa 或ab或者ba 或者c
        f1 = [0,1,2,4]
        ##对于7和9来说,以7为例子
        # 按一次，是p
        #2次，可能是pp或者q
        #3次,可能是‘ppp’，可能是‘pq’，也可能是‘qp’，也可能是‘r’ 
        #按四次 可能是‘pppp’，可能是‘ppq’，也可能是‘pqp’，也可能是‘pr’,
        #可能是‘qpp’，可能是‘qq’，也可能是‘rp’，也可能是‘s’ ，一共八种方案
        f2 = [0,1,2,4,8]
        ##对于递推公式，可以这么理解，对于连续按i次（i大于4），可以分类成以下情况：
        # 先连续按1次，得到一个独立的‘a’，然后剩下的i-1次就查表；
        # 先连续按2次，得到一个独立的‘b’，然后剩下的i-2次就查表；
        # 先连续按3次，得到一个独立的‘c’，然后剩下的i-3次就查表；

        ### 这里先做一个表，如果一个数连续出现 t 次，那么可能的组合数为 f3[t]次 1<= t <=pressedKeys.length
        n = len(pressedKeys)
        ## 为了好遍历，我们把f1与f2补成一样长
        ## 连续按4次2，那么有 7种可能
        f1.append(7)
        for _ in range(5,10**5 + 1): ##连续按5次的可能的情况
            f1.append((f1[-1] + f1[-2] + f1[-3]) % mod) ##这个结果很大，我们先去取模
            f2.append((f2[-1] + f2[-2] + f2[-3] + f2[-4]) % mod)
        
        ###这个表做好后，我们现在对pressKey进行处理     
        ans = 1
        for ch ,s in groupby(pressedKeys):
            m = len(list(s))
            ans = ans*(f2[m] if ch in '79' else f1[m])
        return ans % mod
        ## 

if __name__=='__main__':
    pressedKeys = "222222222222222222222222222222222222"
    a = Solution().countTexts("222222222222222222222222222222222222")
    print(a)
    s = '2266554477'
    for s,ch in groupby(s):
        print(s, list(ch))
    f3 = [1,2,4]
    f4 = [1,1,2,4]
    mod= 1000000007
    for _ in range(10):
        f3.append((f3[-1]+f3[-2]+f3[-3])%mod)
        f4.append((f4[-1]+f4[-2]+f4[-3]+f4[-4])%mod)
    print(f3)