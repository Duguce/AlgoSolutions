class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []
        path = []

        def dfs(start, k, target):
            if k == 0 and target == 0:
                res.append(path[:])
                return
            if k == 0 or target < 0:
                return

            for num in range(start, 10):
                path.append(num)
                dfs(num + 1, k - 1, target - num)
                path.pop()

        dfs(1, k, n)
        return res
