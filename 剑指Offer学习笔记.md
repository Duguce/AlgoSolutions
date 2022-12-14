# 剑指Offer学习笔记

备注：本文中所有的算法实现均基于Python3完成。



## 面试题笔记

### 面试题3：数组中重复的数字

#### 题目一：找出数组中的重复数字

> 问题描述：在一个长度为n的数组里的所有数字都在0~n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}，那么对应的输出是重复的数字2或者3。

- [源码](./solutions-LeetCode/JZ03.py)

- 标签：`数组` `排序` `哈希表`

- 思路一：首先，对输入的数组排序。然后，从头到尾扫描排序后的数组找出重复的数字。

  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(nlogn))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(1))

  - 备注：该解法的复杂度取决于排序数组算法的复杂度。

- 思路二：哈希表。扫描数组中的每个数字，每扫描到一个数字的时候，判断哈希表里是否包含该数字。如果没有，就把数字加入哈希表。如果哈希表中有这个数字，就找到了一个重复的数字。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(n))

- 思路三：类似于原地哈希。由于数组中的数字都在0~n-1的范围内。如果这个数组中没有重复的数字，那么当数组排序之后，数字![公式](https://latex.codecogs.com/svg.image?i)将出现在下标为![公式](https://latex.codecogs.com/svg.image?i)的位置。数组有重复的数字，有些位置可能存在多个数字，同时有些位置可能没有数字。因此，我们可以对数组进行重排。当扫描到下标为![公式](https://latex.codecogs.com/svg.image?i)的数字![公式](https://latex.codecogs.com/svg.image?m)时，首先比较该数字和下标是否相等。如果是，则扫描下一个数字；如果不是，则拿数字![公式](https://latex.codecogs.com/svg.image?m)和下标为![公式](https://latex.codecogs.com/svg.image?m)的数字进行比较。如果它和下标为![公式](https://latex.codecogs.com/svg.image?m)的数字相等，就找到了一个重复的数字；如果它和下标为![公式](https://latex.codecogs.com/svg.image?m)的数字不相等，则把它和下标为![公式](https://latex.codecogs.com/svg.image?m)的数字交换位置。接下来重复这个比较、交换的过程，直到发现一个重复数字为止。

  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n))

  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(1))
  - 备注：该解法是相对最优解法。

#### 题目二：不修改数组找出重复的数字

> 问题描述：在一个长度为n+1的数组里的所有数字都在1~n 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7 的数组{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的输出是重复的数字2或者3。

- 标签：`数组`  `二分查找`
- 思路一：通过创建一个辅助数组，将原数组中的每个数逐一复制到辅助数组中。如果原数组中被复制的数字是m，则把它复制到辅助数组中下标为m的位置，这样就可以发现哪个数字是重复的。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(n))

```python
class Solution:
    # 方法一代码实现
    def findRepeatNumber(self, nums: List[int]) -> int:
        lst = [0] * (len(nums) + 1)
        for n in nums:
            if lst[n] == n:
                return n
            lst[n] = n
```

- 思路二：利用二分的思想，将1-n的数字从中间数字m开始分为两部分，前一半为1-m，后一半为m+1-n，如果1-m中的数字在数组中的次数大于m，那么这一半必有重复的数字；否则，另一部分必定含有重复数字。然后，继续对含有重复数字的区间一分为二，直到找到重复的数字为止。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(nlogn))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(1))
  - 备注：该算法不能保证找出所有重复的数字。

```python
class Solution:
    # 方法二代码实现
    def findRepeatNumber(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left != right:
            mid = ((right - left) >> 1) + left
            count = self.countRange(nums, left, mid)
            # 查看长度为[mid - left + 1]的部分数字出现的次数是否超过该部分的长度
            if count > (mid - left + 1):
                right = mid
            else:
                left = mid + 1
        return left

    def countRange(self, nums, left, right):
        count = 0
        length = len(nums)
        for i in range(length):
            if left <= nums[i] <= right:
                count += 1
        return count
```

### 面试题4：二维数组中的查找

> 问题描述：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

- [源码](./solutions-LeetCode/JZ04.py)
- 标签：`数组` `二分查找` `分治` `矩阵`
- 思路一：首先选取数组中右上角的数字，如果该数字等于要查找的数字，则查找过程结束；如果该数字大于要查找的数字，则剔除这个数字所在的列；如果该数字小于要查找的数字，则剔除这个数字所在的行，知道找到要查找的数字，或查找范围为空。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(m+n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(1))

### 面试题5：替换空格

> 问题描述：请实现一个函数，把字符串中的每个空格替换成"%20"。例如，输入”We are happy.“，则输出”We%20are%20happy.“。

- [源码](./solutions-LeetCode/JZ05.py)
- 标签：`字符串`
- 思路一：通过创建一个新的字符串并在新的字符串上进行替换。遍历输入字符串的每一个字符，当字符为空格时，向新创建的字符串添加“%20”；当字符不为空格时，向新创建的字符串添加该字符。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(n))

- 思路二：先用`split(" ")`以空格为单位进行拆分，然后再利用`"%20".join(s)`对字符串进行拼接。

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        s = s.split(" ")
        return "%20".join(s)
```

- 思路三：双指针，倒序替换。先统计字符串中的空格数量，每替换一个空格，长度增加2，因此替换以后字符串的长度等于原来的长度加上2乘以空格数量。我们准备两个指针，分别等于原始字符串的末尾，拓展后的字符串末尾。如果不是空格，直接替换，如果是空格则替换为“%20”，右边的指针分别向左移动1和3个位置。

### 面试题6：从尾到头打印链表

> 问题描述：输入一个链表的头节点，从尾到头反过来打印出每个节点的值。



## 实用编程思维

- 在面试中要和面试官主动交流，一定要在动手写代码之前弄清楚面试官的需求，包括功能要求和性能要求等；
- 当我们需要解决一个复杂的问题时，一个很有效的办法就是从一个具体的问题入手，通过分析简单具体的例子，试图寻找普遍的规律；
