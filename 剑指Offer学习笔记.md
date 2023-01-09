# 剑指Offer学习笔记

备注：本文中所有的算法实现均基于`Python3`完成。



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

- [源码](./solutions-LeetCode/JZ06.py)
- 标签：`栈` `递归` `链表`

- 思路一：递归法。利用递归，先走至链表末端，回溯时依次将节点值加入列表，这样就可以实现链表值的倒序输出。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(n))

- 思路二：辅助栈法。遍历链表，将各节点值`push`入栈，然后将各节点值pop出栈，存储于数组并返回。（Python直接返回`stack`的倒序列表）
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(n))

### 面试题7：重建二叉树

> 问题描述：输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果都不含重复的数字。例如，输入前序遍历序列{1, 2, 4, 7, 3, 5, 6, 8}和中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}，则重建如下图所示的二叉树并输出它的头结点。

<p align="center"><img src="https://zhgyqc.oss-cn-hangzhou.aliyuncs.com/重建二叉树.JPG" alt="" title="图1 重建的二叉树">
</p>
- [源码](./solutions-LeetCode/JZ07.py)
- 标签：`树` `数组` `哈希表` `分治` `二叉树`
- 思路一：前序遍历的第一个节点一定是二叉树的根节点；在中序遍历中，根节点把中序遍历序列分成了两个部分，左边部分构成了二叉树的根节点的左子树，右边部分构成了二叉树的根节点的右子树；记录根节点在中序遍历中的位置。
- 概念说明
  - 前序遍历：根节点 ==> 左子树节点 ==> 右子树
  - 中序遍历：左子树 ==> 根节点 ==> 右子树
  - 后序遍历：左子树 ==> 右子树 ==> 根节点

### 面试题8：二叉树的下一个节点

> 问题描述：给定一棵二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点？树中的节点除了有两个分别指向左、右子节点的指针，还有一个指向父节点的指针。

- 标签：`树` `数组` `递归`
- 思路一：分类查找法。将节点的情况分为三种。第一种，如果给定的节点有右子节点，则最终要返回的下一个节点是右子树的最左子节点；第二种，如果给定的节点无右子节点，且是当前节点的左子节点，则返回其父节点；第三种，若干给定的节点无右子节点，且当前节点是其父节点的右子节点，则先要沿着父节点爬树，一直爬到当前节点是其父节点的左子节点位置，返回的就是这个父节点。如果没有满足上述情况的则返回NULL。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(1))

```python
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # 如果一个节点有右子树,那么他的下一个节点就是他的右子树的最左子节点
        if pNode.right:
            rchild = pNode.right
            while rchild.left:
                rchild = rchild.left
            return rchild
        
        # 如果一个节点无右子树，且该节点是它父节点的左子节点，那么他的下一个节点就是他的父节点
        if pNode.next and pNode.next.left == pNode:
            return pNode.next
        
        # 如果一个节点既没有右子树，并且它还是它父节点的右子节点
        if pNode.next:
            ppar = pNode.next
            # 沿着左上一直爬树，爬到一个节点是他节点的父节点的的左子节点为止
            while ppar.next and ppar.next.right == ppar:
                ppar = ppar.next
            return ppar.next

        return None
```

- 思路二：首先要根据给定输入中的节点向父级进行迭代，直到找到该树的根节点；然后根据根节点进行中序遍历，当遍历到和给定树节点相同的节点时，下一个节点就是我们的目标返回节点。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(n))

```python
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    nodes = []

    def GetNext(self, pNode):
        # 查找根节点
        root = pNode
        while root.next:
            root = root.next
        
        # 中序遍历打造nodes
        self.InOrder(root)

        # 匹配节点
        for i in range(len(self.nodes) - 1):
            cur = self.nodes[i]
            if pNode == cur:
                return self.nodes[i+1]
        return None
    
    # 中序遍历
    def InOrder(self, root):
        if root == None:
            return
        self.InOrder(root.left)
        self.nodes.append(root)
        self.InOrder(root.right)
```

### 面试题9：栈和队列

> 问题描述：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数`appendTail`和`deleteHead`，分别完成在队列尾部插入节点和在队列头部删除节点的功能。

- [源码](./solutions-LeetCode/JZ09.py)
- 标签：`栈` `设计` `队列`
- 思路一：本题要求利用双栈实现队列的`appendTail`和`deleteHead`两个函数功能，因此，我们可以设计一个`stk_in`栈和一个`stk_out`栈。
  - 加入队尾`appendTail`函数：将值`value`加入栈`stk_in`即可。
  - 删除队首`deleteHead`函数：当栈`stk_out`为空时，将栈`stk_in`中的元素全部转移至栈`stk_out`中，实现元素倒序，并返回`stk_out`的栈顶元素；当栈`stk_out`不为空时，直接返回栈`stk_out`的栈顶元素；否则，当两个栈都为空时，返回`-1`。


- 时间复杂度：`appendTail()`函数为![时间复杂度](https://latex.codecogs.com/svg.image?O(1))；`deleteHead()`函数在N次队首元素删除操作中总共需要完成N个元素的倒序。
- 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(n))

### 面试题10：斐波那契数列

#### 题目一：求斐波那契数列的第n项

> 问题描述：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。斐波那契数列的定义如下：

<p align="center"><img src="https://zhgyqc.oss-cn-hangzhou.aliyuncs.com/fibonacci.JPG" alt="" title="fibonacci">
</p>
- [源码](./solutions-LeetCode/JZ10.py)
- 标签：`记忆化搜索` `数学` `动态规划`
- 思路一：递归法。把f_n问题的计算拆分成f(n-1)和f(n-2)两个子问题的计算，并递归，以f(0)和f(1)为终止条件（*<u>该方法的缺点在于需要大量的重复计算</u>*）。

```python
class Solution:
    # 递归法（该代码会超时）
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return (self.fib(n-1) + self.fib(n-2))%1000000007
```

- 思路二：递归法。以斐波那契数列性质 *f*(*n*+1)=*f*(*n*)+*f*(*n*−1) 为转移方程。

```python
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            b = a + b
            a = b - a
        return a % 1000000007
```

#### 题目二：青蛙跳台阶问题

> 问题描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级台阶总共有多少种跳法。
>

```python
class Solution:
    def numWays(self, n: int) -> int:
        x, y = 1, 1
        for _ in range(n):
            x, y = y, x+y
        return x % 1000000007
```

### 面试题11：旋转数组的最小数字

> 问题描述：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组{3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该数组的最小值为1。

- [源码](./solutions-LeetCode/JZ11.py)
- 标签：`数组` `二分查找`
- 思路一：二分查找。旋转数组可以看作两个排序数组，而寻找旋转数组的最小元素即为寻找右排序数组的最小元素。我们可以声明两个索引`left`，`right`分别指向`nums`数组的左右两端。然后进行循环二分，设`mid=(i+j)//2`为每次二分的终点，具体可以分为以下三种情况，①当`nums[left]>nums[right]`时，`mid`一定在左排序数组中，此时执行`left=mid+1`；②当`nums[left]<nums[right]`时，`mid`一定在右排序数组中，此时执行`right=mid`；③当`nums[left]=nums[right]`时，执行`right=right-1`。当`left=right`时跳出循环，并返回旋转点的值`nums[left]`。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(logn))，在特例情况下会退化到![时间复杂度](https://latex.codecogs.com/svg.image?O(n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(1))

### 面试题12：矩阵中的路径

> 问题描述：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用下画线标出）。但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
>













## 实用编程思维

- 在面试中要和面试官主动交流，一定要在动手写代码之前弄清楚面试官的需求，包括功能要求和性能要求等；
- 当我们需要解决一个复杂的问题时，一个很有效的办法就是从一个具体的问题入手，通过分析简单具体的例子，试图寻找普遍的规律；
