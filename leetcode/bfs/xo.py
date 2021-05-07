class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not (board and board[0]):
            return
        
        i = len(board)
        j = len(board[0])
        to_reach = [(0, x) for x in range(j)] + [(i-1, x) for x in range(j)] + [(x, 0) for x in range(i)] + [(x, j-1) for x in range(i)]
        reached = []
        while to_reach:

            point = to_reach.pop(0)
            
            if point in reached:
                continue
            
            if board[point[0]][point[1]] == "O":
                board[point[0]][point[1]] = "A"
                # reached.append(point) # 列表中in的操作是遍历列表，比较耗时，用替换方法反而省时间 
                reached.append(point)
            else:
                reached.append(point)
                continue
            
            to_reach.append((max(point[0]-1, 0), point[1]))
            to_reach.append((min(point[0]+1, i-1), point[1]))
            to_reach.append((point[0], max(point[1]-1, 0)))
            to_reach.append((point[0], min(point[1]+1, j-1)))

        for x in range(i):
            for y in range(j):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "A":
                    board[x][y] = "O"
        

    def solve2(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not (board and board[0]):
            return
        
        i = len(board)
        j = len(board[0])
        reached = []
        def dfs(point):
            if point in reached:
                return
            reached.append(point)
            if board[point[0]][point[1]] == "O":
                board[point[0]][point[1]] = "A"
            
                dfs((max(point[0]-1, 0), point[1]))
                dfs((min(point[0]+1, i-1), point[1]))
                dfs((point[0], max(point[1]-1, 0)))
                dfs((point[0], min(point[1]+1, j-1)))
        for p in [(0, x) for x in range(j)] + [(i-1, x) for x in range(j)] + [(x, 0) for x in range(i)] + [(x, j-1) for x in range(i)]:
            dfs(p)

        for x in range(i):
            for y in range(j):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "A":
                    board[x][y] = "O"
        


Solution().solve2([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])