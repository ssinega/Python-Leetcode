class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

          
            grid[r][c] = 0

            
            area = 1
            area += dfs(r + 1, c)  
            area += dfs(r - 1, c) 
            area += dfs(r, c + 1) 
            area += dfs(r, c - 1)  

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_area = dfs(r, c)
                    max_area = max(max_area, current_area)

        return max_area
