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

<p align="center"><img src="https://zhgyqc.oss-cn-hangzhou.aliyuncs.com/矩阵中的路径.JPG" alt="" title="path_of_matrix">
</p>

- [源码](./solutions-LeetCode/JZ12.py)
- 标签：`数组` `回溯` `矩阵` `DFS`
- 思路一：本问题是典型的矩阵搜索问题，可以使用深度优先搜索（DFS）+剪枝的方法解决。深度优先搜索可以理解为暴力法遍历矩阵中所有字符串的可能性。DFS通过递归，先朝一个方向搜索到底，再回溯至上个节点，沿另一个方向搜索，以此类推。在搜索过程中，遇到这条路不可能与目标字符串匹配成功的情况，则应立即返回，称之为可行性剪枝。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(3^KMN))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(K))

### 面试题13：机器人的运动范围

> 问题描述：地上有一个m行n列的方格。一个机器人从坐标(0, 0)的格子开始移动，它每次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格(35, 37)，因为3+5+3+7=18。但它不能进入方格(35, 38)，因为3+5+3+8=19。请问该机器人能够到达多少个格子。

- [源码](./solutions-LeetCode/JZ13.py)
- 标签：`回溯` `矩阵` `DFS`
- 思路一：从[0,0]开始，每次选择一个方向开始检查能否访问，如果能访问进入该节点，该节点作为子问题，继续按照这个思路访问，一条路走到黑，然后再回溯，回溯的过程中每个子问题再选择其他方向，正是深度优先搜索。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(MN))，其中*m*与*n*分别为格子的边长，深度优先搜索最坏情况下遍历格子每个位置一次
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(MN))

```python
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def getDigitSum(i, j):
            res = 0
            while i:
                res += i % 10
                i //= 10
            while j:
                res += j % 10
                j //= 10
            return res

        visited = set()

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or getDigitSum(i, j) > k or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i, j + 1) + dfs(i + 1, j)

        return dfs(0, 0)
```

### 面试题14：剪绳子

> 问题描述：给你一根长度为*n*的绳子，请把绳子剪成*m*段（*m*、*n*都是整数，*n>1*并且*m>1*），每段绳子的长度记为*k[0], k[1], ..., k[m]*。请问*k[0]×k[1]× ...×k[m]*可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

- [源码](./solutions-LeetCode/JZ14.py)

- 标签：`数学` `动态规划` `贪心算法`

- 思路一：动态规划。本题给定一个大于1的正整数*n*，要求将*n*拆分成至少两个整数的和，并使这些正整数的乘积最大化，返回最大成绩值。令*x*是拆分出的第一个正整数，则剩下的部分是*n - x*，*n - x*可以不继续拆分，或者继续拆分成至少两个正整数的和。由于每个正整数对应的最大乘积取决于比它小的正整数对应的最大乘积，因此可以使用动态规划求解。创建数组*dp*，其中*dp[i]*表示将正整数*i*拆分成至少两个正整数的和之后，这些正整数的最大乘积。特别地，0不是正整数，1是最小正整数，0和1都不能拆分，因此*dp[0] = dp[1] = 0*。当*i >= 2*时，假设对正整数*i*拆分出的第一个正整数是*j*（1 <= j < i），则有以下两种方案：将*i*拆分成*j*和*i - j*的和，且*i - j*不再拆分成多个正整数，此时的乘积是*j × (i - j)*；将*i*拆分成*j*和*i - j*的和，且*i - j*继续拆分成多个正整数，此时的乘积是*j × dp[i - j]*。因此，当*j*固定时，有*dp[i] = max(j × (i - j), j × dp[i - j])*。由于*j*的取值范围是1到*i - 1*，需要遍历所有的*j*得到*dp[i]*的最大值，因此可以得到的状态转移方程如下：
  $$
  dp[i] = max_{1\leq j<i} \{max(j\times(i - j), j\times dp[i - j])\}
  $$

  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n^2))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(n))

- 思路二：贪心算法。核心思路是尽可能地将绳子分为长度为3的小段，这样乘积最大。具体步骤如下：当*n<=3*时，返回*n-1*，当*n=4*时，返回4，当*n>=5*时，尽可能多地剪长度为3的绳子。

  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(1))


```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        times_of_3 = n // 3
        if n - times_of_3 * 3 == 0:
            return int(math.pow(3, times_of_3))
        if n - times_of_3 * 3 == 1:
            return int(math.pow(3, times_of_3 - 1) * 4)
        return int(math.pow(3, times_of_3) * 2)
```

### 面试题15：二进制中1的个数

> 问题描述：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如，把9表示成二进制是1001，有2位是1。因此，如果输入9，则该函数输出2。

- [源码](./solutions-LeetCode/JZ15.py)
- 标签：`位运算`
- 思路一：巧用*n&(n-1)*。*n&(n-1)*的结果恰为把*n*的二进制位中的最低位的1变为0之后的结果，在实际代码中，我们不断让当前的*n*与*n-1*做与运算，直到*n*变为0即可。因为每次运算会使得*n*的最低位的1被翻转，因此运算次数就等于*n*的二进制位中1的个数。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(logn))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(1))

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1

        return res
```

### 面试题16：数值的整数次方

> 问题描述：实现函数double Power (double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

- [源码](./solutions-LeetCode/JZ16.py)
- 标签：`递归` `数学`

- 思路一：快速幂法。假设输入的指数exponent为32，即目标是求出一个数字的32次方，如果我们已经知道了它的16次方，那么只要在16次方的基础上再平方一次就可以了。而16次方是8次方的平方。这样以此类推，求32次方只需要做5次乘法：先求平方，在平方的基础上求4次方，在4次方的基础上求8次方，在8次方的基础上求16次方，最后在16次方的基础上求32次方。也就是说，我们可以用如下公式求*a*的*n*次方：
  $$
  a^n=\begin{cases}
  a^{n/2}\cdot a^{n/2} &\text{n为偶数}\\
  a^{(n-1)/2}\cdot a^{n/2}\cdot a &\text{n为奇数}\\
  \end{cases}
  $$

  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(logn))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(1))

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            x, n = 1 / x, -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
```

### 面试题17：打印从1到最大的n位数

> 问题描述：输入数字n，按顺序打印出从1到最大的n位十进制数。比如输入3，则打印1、2、3一直到最大的3位数999。
>

- [源码](./solutions-LeetCode/JZ17.py)
- 标签：`数组` `数学`
- 思路一：由于本题没有限定*n*的范围，因此我们需要考虑大数越界的情况。解决大数问题最常用的方法就是使用字符串或者数组。在用字符串表示数字的时候，最直观的方法就是字符串里每个字符都是，0〜9，之间的某一个字符，用来表示数字中的一位。如果我们在数字前面补0，就会发现*n*位所有十进制数其实就是*n*个从0到9的全排列。也就是说，我们把数字的每一位都从0到9排列一遍，就得到了所有的十进制数。
  - 时间复杂度：![时间复杂度](https://latex.codecogs.com/svg.image?O(10^n))
  - 空间复杂度：![空间复杂度](https://latex.codecogs.com/svg.image?O(10^n))

```python
class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(int(s))
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1
        
        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res
```

### 面试题18：删除链表的节点

#### 题目一：删除链表节点

> 问题描述：给定单向链表的头指针和一个节点指针，定义一个函数删除该节点。

- [源码](./solutions-LeetCode/JZ18.py)
- 标签：`链表`
- 思路一：要删除给定单向链表中的某个节点，只需要进行两步操作。一是，找到待删除节点的前一个节点；二是将pre-->next设置为pre->next->next。

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        pre = head
        while pre.next and pre.next.val != val:
            pre = pre.next
        if pre.next:
            pre.next = pre.next.next
        return head
```

#### 题目二：删除链表中重复的节点

> 问题描述：在一个排序的链表中，如何删除重复的节点。

- 标签：`链表`
- 思路一：首先检查链表是否为空或只有一个节点。如果是，则无需删除重复元素，直接返回链表头节点。定义两个指针：prev和curr。prev指向前一个节点，curr指向当前节点。初始时，prev指向头节点，curr指向第二个节点。遍历链表，直到curr到达链表尾部。在每一步迭代中，检查curr和prev节点的值是否相等。如果相等，则将prev的next指针跳过curr，使prev的next指向curr的next，以删除curr节点。否则，将prev和curr指针都向前移动一个节点。最后，返回头节点。

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 如果链表为空或只有一个节点，则无重复节点需要删除
        if not head or not head.next:
            return head

        # 初始化双指针，一个指向前一个节点，一个指向当前节点
        prev = head
        curr = head.next

        # 遍历链表
        while curr:
            # 如果当前节点的值等于前一个节点的值，则说明当前节点是重复节点，需要删除
            if curr.val == prev.val:
                # 删除当前节点
                prev.next = curr.next
                curr = curr.next
            else:
                # 不是重复节点，将双指针都向前移动
                prev = curr
                curr = curr.next
        return head
```

### 面试题19：正则表达式匹配

> 问题描述：请实现一个函数用来匹配包含'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'\*\'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab\*ac\*a"匹配，但与"aa.a"和"ab\*a"均不匹配。

- [源码](./solutions-LeetCode/JZ19.py)
- 标签：`递归` `字符串` `动态规划`
- 思路一：设$$s$$（字符串）的长度为$$n$$，$$p$$（模式字符串）的长度为$$m$$；将$$s$$的第$$i$$个字符记为$$s_i$$，$$p$$的第$$j$$个字符记为$$p_j$$，将$$s$$的前$$i$$个字符组成的子字符串记为$$s[:i]$$，同理将$$p$$的前$$j$$个字符组成的子字符串记为$$p[:j]$$。因此本题可转化为求$$s[:n]$$是否能和$$p[:m]$$匹配。从$$s[:1]$$和$$p[:1]$$开始判断是否能匹配，每轮添加一个字符并判断是否能够匹配，直至添加完整个字符串$$s$$和$$p$$。
  - 时间复杂度：$$O(MN)$$
  - 空间复杂度：$$O(MN)$$


```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.') if p[
                                                                                                             j - 1] == '*' else \
                    dp[i - 1][j - 1] and (p[j - 1] == '.' or s[i - 1] == p[j - 1])

        return dp[-1][-1]
```





## 实用编程思维

- 在面试中要和面试官主动交流，一定要在动手写代码之前弄清楚面试官的需求，包括功能要求和性能要求等；
- 当我们需要解决一个复杂的问题时，一个很有效的办法就是从一个具体的问题入手，通过分析简单具体的例子，试图寻找普遍的规律；
- 除法的效率比移位运算要低得多，在实际编程中应尽可能地用移位运算符代替乘除法。
