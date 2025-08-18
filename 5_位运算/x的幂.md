推广到任意数的幂

给定一个整数 n 判断n 是否是 a 的幂次方。

==> 也就是说是否存在 整数 x 使得 n == a<sup>x</sup>

==> 两边同时取对数 ==》等价于:是否存在整数x 使得lg(n) == xlg(a) 成立(当然这里我们默认了 n 是大于 0 的也就是 底数 a是大于0 的)

===> 等价于 x = lg(n) / lg(a) 是否是一个整数
===> 等价于 lg(n) / lg(a) % 1 == 0 ？

[leetcode231](https://leetcode.cn/problems/power-of-two/description/)

```python
import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (math.log10(n) / math.log10(2)) % 1 == 0
```
[leetcode342](https://leetcode.cn/problems/power-of-four/description/)

```python
import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (math.log10(n) / math.log10(4)) % 1 == 0
```
