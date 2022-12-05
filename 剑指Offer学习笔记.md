# 剑指Offer学习笔记

备注：本文中所有的算法实现均基于Python3完成。



## 面试题笔记

### 题目3：数组中重复的数字

> 问题描述：在一个长度为n的数组里的所有数字都在0~n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2, 3, 1,0, 2, 5, 3}，那么对应的输出是重复的数字2或者3。

- [源码](./solutions-LeetCode/JZ03.py)

- 标签：`数组` `排序` `哈希表`

- 方法一：首先，对输入的数组排序。然后，从头到尾扫描排序后的数组找出重复的数字。

  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(nlogn))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(1))

  - 备注：该解法的复杂度取决于排序数组算法的复杂度。

- 方法二：哈希表。扫描数组中的每个数字，每扫描到一个数字的时候，判断哈希表里是否包含该数字。如果没有，就把数字加入哈希表。如果哈希表中有这个数字，就找到了一个重复的数字。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(n))

- 方法三：类似于原地哈希。由于数组中的数字都在0~n-1的范围内。如果这个数组中没有重复的数字，那么当数组排序之后，数字![公式](https://latex.codecogs.com/svg.image?i)将出现在下标为![公式](https://latex.codecogs.com/svg.image?i)的位置。数组有重复的数字，有些位置可能存在多个数字，同时有些位置可能没有数字。因此，我们可以对数组进行重排。当扫描到下标为![公式](https://latex.codecogs.com/svg.image?i)的数字![公式](https://latex.codecogs.com/svg.image?m)时，首先比较该数字和下标是否相等。如果是，则扫描下一个数字；如果不是，则拿数字![公式](https://latex.codecogs.com/svg.image?m)和下标为![公式](https://latex.codecogs.com/svg.image?m)的数字进行比较。如果它和下标为![公式](https://latex.codecogs.com/svg.image?m)的数字相等，就找到了一个重复的数字；如果它和下标为![公式](https://latex.codecogs.com/svg.image?m)的数字不相等，则把它和下标为![公式](https://latex.codecogs.com/svg.image?m)的数字交换位置。接下来重复这个比较、交换的过程，直到发现一个重复数字为止。

  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n))

  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(1))
  - 备注：该解法是相对最优解法。



### 题目4：不修改数组找出重复的数字

> 在一个长度为n的数组里的所有数字都在0~n 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7 的数组{2, 3, 1,0, 2, 5, 3}，那么对应的输出是重复的数字2或者3。