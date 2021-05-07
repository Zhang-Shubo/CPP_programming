class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        if not (grid and grid[0]):
            return 0
        i = len(grid)
        j = len(grid[0])
        num = 0
        nums = [0]
        def dfs(point):
            if grid[point[0]][point[1]] == "1":
                grid[point[0]][point[1]] = "2"
                ps = [(point[0], point[1]+1), (point[0], point[1]-1), (point[0]-1, point[1]), (point[0]+1, point[1])]
                for x,y in ps:
                    if -1<x<i and -1<y<j:
                        dfs((x, y))
                num += 1

        for x in range(i):
            for y in range(j):
                if grid[x][y] == "1":
                    num = 0
                    dfs((x, y))
                    nums.append(num)
        return max(nums)